
## Description
지뢰찾기 API 입니다. 실제로 구현한다면 프론트에서 obfuscate된 코드를 사용해서
많은 부분을 만들겠지만 프론트에서 제어 가능한 몇몇 validation들을 제외하고는 모두
API를 통해 소통한다고 가정하고 만들어 보았습니다.



## Features
* 난이도는 "easy", "medium", "hard" 및 "custom" 모드가 있습니다.
* /new_game을 통해 새로운 게임을 생성하지만 첫 번째 클릭은 무조건 💣이 아니도록 맵이 재조정됩니다.
* 좌클릭 (셀 오픈)
* 우클릭 (🚩 플래그 기능)
* 좌우 한번에 클릭 (해당 셀의 숫자와 주변 💣 수가 일치할 경우 인접한 셀들 중 오픈되지 않은 셀들을 모두 오픈
* 이 경우 깃발이 잘못 표시되어 있으면 게임 종료
* 이벤트 발생시마다 게임 종료되었는지 체크
* 게임이 종료되었다면 is_finished가 True로 변하며 더 이상 게임 진행 불가
* response는 player_map, 즉 가려진 상태로만 전송됩니다.
* 우클릭을 제외한 모든 이벤트 발생시 게임이 종료되었는지 판단합니다

## Controls
  
* 좌클릭 to reveal cell<br>
* 우클릭 to flag (깃발)
* 좌우 한번에 클릭해서 모두 오픈

## Future
* API에는 반영되어 있지 않지만 클릭 수로 clicks 및 효율성을 return할 수 있습니다
* Game 모델의 created_at과 updated_at 차이를 통해 쉽게 duration을 return할 수 있습니다
