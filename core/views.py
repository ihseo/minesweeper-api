from core.models import (Game,
                         Map,)
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from core.logics import (create_map,
                         left_click,
                         right_click,
                         left_right_click)
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from core.serializers import GameSerializer


class GameList(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    @swagger_auto_schema(responses={200: GameSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class NewGame(APIView):
    """
    새로운 게임을 생성합니다.
    """
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={'width': openapi.Schema(type=openapi.TYPE_INTEGER, description='width 값'),
                    'height': openapi.Schema(type=openapi.TYPE_INTEGER, description='height 값'),
                    'mines': openapi.Schema(type=openapi.TYPE_INTEGER, description='지뢰 수'),
                    'difficulty': openapi.Schema(type=openapi.TYPE_STRING, description='난이도', example='easy', enum=['easy', 'normal', 'hard', 'custom']),
                    }))
    def post(self, request):
        difficulty = request.data.get('difficulty')
        width = request.data.get('width')
        height = request.data.get('height')
        mines = request.data.get('mines')
        ms_map = create_map(difficulty, width=width, height=height, mines=mines)
        game = Game.objects.create(
            map=ms_map,
            width=width,
            height=height,
            mines=mines,
        )
        return Response({'game_id': game.id}, status=status.HTTP_201_CREATED)


class LeftClick(APIView):
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={'y': openapi.Schema(type=openapi.TYPE_INTEGER, description='width 값'),
                    'x': openapi.Schema(type=openapi.TYPE_INTEGER, description='height 값'),
                    'is_first_move': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='지뢰 수'),
                    }))
    def post(self, request, pk):
        y = request.data.get('y')
        x = request.data.get('x')
        is_first_move = request.data.get('is_first_move')
        game = Game.objects.get(id=pk)
        if game.is_over:
            return Response({'message': '이미 종료된 게임입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        if is_first_move:
            ms_map = game.map
        else:
            ms_map = game.maps.last().map  # first move가 아닐 경우 마지막 move를 통해 만들어진 map을 가져옴
        print('game map:', game.map)
        ms_map, game_status = left_click(ms_map, y, x, is_first_move)
        Map.objects.create(game=game, map=ms_map)
        if game_status == 'over':
            game.is_over = True
            game.save()
        if game_status == 'clear':
            game.is_over = True
            game.is_won = True
            game.save()
        return Response({'map': create_player_map(ms_map), 'game_status': game_status}, status=status.HTTP_200_OK)


class RightClick(APIView):
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={'y': openapi.Schema(type=openapi.TYPE_INTEGER, description='width 값'),
                    'x': openapi.Schema(type=openapi.TYPE_INTEGER, description='height 값'),
                    }))
    def post(self, request, pk):
        y = request.data.get('y')
        x = request.data.get('x')
        game = Game.objects.get(id=pk)
        if game.maps.last():
            ms_map = game.maps.last().map
        else:
            ms_map = game.map
        ms_map = right_click(ms_map, y, x)
        Map.objects.create(game=game, map=ms_map)
        return Response({'map': create_player_map(ms_map)}, status=status.HTTP_200_OK)


class LeftRightClick(APIView):
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={'y': openapi.Schema(type=openapi.TYPE_INTEGER, description='width 값'),
                    'x': openapi.Schema(type=openapi.TYPE_INTEGER, description='height 값'),
                    }))
    def post(self, request, pk):
        y = request.data.get('y')
        x = request.data.get('x')
        game = Game.objects.get(id=pk)
        if game.maps.last():
            ms_map = game.maps.last().map
        else:
            ms_map = game.map
        ms_map, game_status = left_right_click(ms_map, y, x)
        Map.objects.create(game=game, map=ms_map)
        return Response({'map': create_player_map(ms_map), 'game_status': game_status}, status=status.HTTP_200_OK)


def create_player_map(minesweeper_map):
    height = len(minesweeper_map[0])
    width = len(minesweeper_map)
    player_map = [[0] * height for _ in range(width)]
    for x in range(height):
        for y in range(width):
            if minesweeper_map[y][x][1] in ['C', 'F']:
                player_map[y][x] = minesweeper_map[y][x][1]
            else:
                player_map[y][x] = minesweeper_map[y][x][0]
    return player_map
