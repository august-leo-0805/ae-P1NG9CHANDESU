# ae-P1NG9CHANDESU
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![discord.py](https://img.shields.io/badge/discord.py-v2.3%2B-5865F2?style=flat-square&logo=discord&logoColor=white)](https://github.com/Rapptz/discord.py)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Permissions](https://img.shields.io/badge/Permission-Administrator-red?style=flat-square&logo=discord&logoColor=white)](#)
[![Discord Invite](https://img.shields.io/badge/Discord-Invite%20Bot-5865F2?style=flat-square&logo=discord&logoColor=white)](여기에_봇_초대_링크_주소)

**æ-P1NG9CHANDESU**는 디스코드 서버 관리, 자동 로깅, 동적 음성 채널 생성, 문의 티켓 시스템, 스팸 방지 및 이모지 관리 기능을 제공하는 종합 디스코드 봇 프로젝트입니다.

## 주요 기능 (Features)
봇의 주요 기능은 아래와 같습니다.

### 1. 서버 설정 (`Settings Cog`)
* 서버별 설정 데이터(`config.json`)를 독립적으로 저장하고 관리합니다.
* 명령어 채널, 이모지 전용 채널, 스팸 감지 채널, 음성 생성 채널, 로그 채널 등을 개별 지정할 수 있습니다.
* `/check` 명령어로 현재 서버의 전체 설정 상태를 조회합니다.

### 2. 서버 관리 및 처벌 (`Moderation Cog`)
* **음성 채널 제어:** 마이크 차단(`/mute`, `/unmute`), 헤드셋 차단(`/deafen`, `/undeafen`), 음성 강제 퇴장(`/vckick`).
* **서버 제재:** 타임아웃(`/timeout`, `/untimeout`), 추방(`/kick`), 차단(`/ban`, `/unban`).
* **유연한 시간 단위:** `10s`(초), `5m`(분), `1h`(시간), `1d`(일) 시간 파싱 지원.

### 3. 로깅 시스템 (`Logger Cog`)
* **입퇴장 기록:** 멤버 입장 및 퇴장 로그.
* **메시지 변동:** 메시지 수정(수정 전/후 비교) 및 삭제 로그.
* **음성 채널 이동:** 음성 채널 입장/퇴장/채널 간 이동 실시간 감지.
* **이모지 변경 감지:** 서버 이모지 추가, 삭제, 이름 변경 내역 감지 및 감사 로그(Audit Log) 연동.

### 4. 동적 음성 채널 (`Voice Cog`)
* **방 만들기 음성 채널:** 지정된 생성 채널 입장 시 개인 전용 임시 음성 채널이 자동 생성되고 이동됩니다.
* **방장 권한 부여:** 채널을 생성한 유저에게 해당 임시 음성 채널의 관리 권한 부여.
* **자동 삭제:** 채널 인원이 0명이 되면 자동으로 채널 삭제 및 정리.
* **방장 전용 명령어:** 슬래시 명령어(`/named`, `/limit`)로 채널명 및 인원 제한 설정 가능.

### 5. 문의 티켓 시스템 (`Ticket Cog`)
* **버튼 기반 패널:** 설정된 안내 패널의 버튼 클릭으로 개별 문의 채널 생성.
* **자동 종료 타이머:** 5분간 대화가 없을 시 자동으로 채널 닫힘 및 `closed` 카테고리 이동.
* **관리자 전용 답변:** `/answer` 명령어로 관리자가 지정된 티켓 채널에 개별 답변 작성 가능.
* **티켓 전용 로그:** 티켓 채널 내부 대화 및 첨부파일 내역을 지정된 로그 채널로 전송.

### 6. 스팸 방지 및 자동 모더레이션 (`Spam Cog`)
* **스팸 감지 채널:** 지정된 스팸 채널에 메시지 작성 시 해당 유저를 1일간 임시 차단(Temp Ban) 후 자동 해제.
* **전체 멘션 제재:** 일반 유저의 `@everyone` / `@here` 멘션 감지 시 메시지 삭제 및 1시간 타임아웃 처벌.

### 7. 이모지 도우미 (`Emoji Helper Cog`)
* **이모지 확대 (Emoji Enlarger):** 메시지에 단일 이모지만 포함된 경우, 웹훅을 활용해 고화질 이미지로 확대 전송.
* **커스텀 이모지 등록/삭제:** 첨부파일, URL, 타 서버 이모지를 활용한 이모지 추가(`/addemoji`) 및 삭제(`/delemoji`).

## 프로젝트 구조 (Project Structure)
```
.
├── cogs/                               # 기능별 Cog 모듈
│   ├── emoji.py                        # 이모지 확대 및 등록/삭제
│   ├── moderation.py                   # 서버 관리 및 제재 명령어
│   ├── logger.py                       # 서버 이벤트 로그
│   ├── settings.py                     # 서버 설정 및 명령어 그룹
│   ├── spam.py                         # 스팸 감지 및 차단 자동화
│   ├── ticket.py                       # 문의 티켓 시스템
│   └── voice.py                        # 동적 음성 채널 생성 및 제어
├── data/                               # 서버 데이터 저장 폴더 (실행 시 자동 생성)
│   ├── config.example.json             # 서버 설정 JSON 데이터 예시 템플릿
│   ├── config.json                     # 서버별 채널 및 티켓 설정 데이터
│   ├── spam_ban.example.json           # 스팸 차단 JSON 데이터 예시 템플릿
│   ├── spam_ban.json                   # 스팸 필터 임시 차단 유저 및 만료 시간 정보
│   ├── temp_channels.example.json      # 임시 음성 채널 JSON 데이터 예시 템플릿
│   └── temp_channels.json              # 생성된 임시 음성 채널 및 방장 정보
├── .env                                # 봇 토큰 등 보안 환경 변수 파일 (Git 추적 제외)
├── .env.example                        # 환경 변수 설정 템플릿 (토큰 양식)
├── .gitignore                          # Git 추적 제외 설정 파일 (.env, data/*.json 등)
├── main.py                             # 봇 메인 실행 파일
└── requirements.txt                    # 의존성 패키지 목록
```

## 데이터 파일 구조 및 역할 (`data/*.json`)
봇 실행 시 `data/` 디렉터리에 자동으로 생성 및 업데이트되는 JSON 파일들의 역할과 구조입니다.

### 1. `data/config.json` (서버 설정 데이터)
각 디스코드 서버(Guild ID)별 지정된 로그 채널, 스팸 감지 채널, 음성 생성 채널 ID 및 티켓 패널 정보를 관리합니다.
* **주요 필드:**
  * `spam_filter_channel_id`: 스팸 감지 텍스트 채널 ID
  * `create_voice_channel_id`: 동적 음성 방 생성용 음성 채널 ID
  * `server_log_channel_id` / `punish_log_channel_id` / `ticket_log_channel_id`: 각 로그 채널 ID
  * `ticket_panel_channel_id` / `ticket_panel_msg_id`: 생성된 티켓 안내 패널 위치
  * `ticket_count`: 서버별 누적 생성 티켓 수

### 2. `data/temp_channels.json` (임시 음성 채널 데이터)
동적 생성된 음성 채널의 ID와 채널을 소유한 방장(User ID)을 매핑하여 저장합니다. 봇이 재시작되어도 방장 권한 명령어나 자동 삭제 로직이 정상 작동하도록 보장합니다.
* **구조:** `{ "서버_ID": { "생성된_음성채널_ID": "방장_유저_ID" } }`

### 3. `data/spam_ban.json` (스팸 임시 차단 데이터)
스팸 감지 채널 이용으로 인해 1일 임시 차단(Temp Ban)된 유저들의 차단 해제 시간(UNIX Timestamp)을 관리합니다. 백그라운드 루프 Task가 해당 시각을 감지하여 차단을 자동 해제합니다.
* **구조:** `{ "서버_ID": { "차단된_유저_ID": 차단해제_타임스탬프(float) } }`

## 봇 초대 및 권한 안내 (Bot Invite & Permissions)
본 봇은 음성 채널 자동 생성, 이모지 관리, 스팸 필터링, 로깅 등 서버 전체의 제어 기능을 포함하고 있으므로 **관리자(Administrator)** 권한이 필요합니다.

* **[봇 초대하기 (관리자 권한 포함)](여기에_봇_초대_링크_주소)**
    * **참고:** 위 링크에는 이미 `administrator` 권한(권한 비트 `8`) 및 `applications.commands` 스코프가 설정되어 있어, 서버 선택 후 승인만 진행하시면 됩니다.

## 설치 및 실행 방법 (Setup)
봇을 설치하고 실행하는 단계별 가이드입니다.

### 1. 요구 사항 (Prerequisites)
* **Python 3.10** 이상

### 2. 저장소 가져오기
```bash
git clone https://github.com/penguinjean0421/ae-P1NG9CHANDESU.git
cd ae-P1NG9CHANDESU
```

### 3. 필수 라이브러리 설치
프로젝트 루트 디렉터리에서 `requirements.txt`를 통해 의존성 패키지를 일괄 설치합니다.

```bash
pip install -r requirements.txt
```

### 4. 디스코드 개발자 센터 설정 (Developer Portal)
디스코드 개발자 콘솔의 **Bot > Privileged Gateway Intents** 섹션에서 다음 항목을 반드시 활성화(**ON**)해야 합니다.

* 🟢 **SERVER MEMBERS INTENT** (멤버 입장/퇴장 감지)
* 🟢 **MESSAGE CONTENT INTENT** (스팸 감지, 메시지 로그 및 이모지 확대 기능)

### 5. 환경 변수 (`.env`) 설정
프로젝트 루트 디렉터리에 `.env` 파일을 생성하고 발급받은 디스코드 봇 토큰을 입력합니다.

```env
# Discord Bot Configuration
# [REQUIRED] Your Discord Bot Token (https://discord.com/developers/applications)
BOT_TOKEN=your_discord_bot_token_here

# [OPTIONAL] Command prefixes, separated by commas if multiple (Default: !)
BOT_PREFIXES=!, ?
```

### 6. 봇 실행
```bash
python main.py
```

## 주요 명령어 안내 (Commands List)
봇에서 제공하는 슬래시 명령어 목록입니다.

### 서버 설정 (`/set`, `/reset`, `/check`)
| 명령어 | 설명 | 비고 |
| ----- | ----- | ----- |
| `/check` | 현재 서버의 채널 설정 상태 조회 | 관리자 전용 |
| `/set log [server\|punish\|ticket]` | 각 카테고리별 로그 채널 지정 | 관리자 전용 |
| `/set command [bot\|ticket]` | 봇 명령어 채널 지정 또는 티켓 패널 생성 | 관리자 전용 |
| `/set spam` | 스팸 감지 채널 지정 | 관리자 전용 |
| `/set voice` | 방 만들기 음성 채널 지정 | 관리자 전용 |
| `/reset [all\|log\|command\|voice\|spam]` | 지정된 서버 설정 초기화 | 관리자 전용 |

### 서버 관리 (`/moderation`)
| 명령어 | 설명 | 비고 |
| ----- | ----- | ----- |
| `/mute`, `/unmute` | 음성 마이크 차단 / 해제 | 관리자 전용 |
| `/deafen`, `/undeafen` | 음성 헤드셋 차단 / 해제 | 관리자 전용 |
| `/vckick` | 음성 채널 강제 퇴장 | 관리자 전용 |
| `/timeout`, `/untimeout` | 타임아웃 적용 / 해제 | 관리자 전용 |
| `/kick`, `/ban`, `/unban` | 유저 추방 / 차단 / 차단 해제 | 관리자 전용 |

### 임시 음성 채널 (`/voice`)
| 명령어 | 설명 | 비고 |
| ----- | ----- | ----- |
| `/named` | 현재 접속한 임시 음성 채널의 이름 변경 | 방장 전용 |
| `/limit` | 현재 접속한 임시 음성 채널의 인원 제한 변경 | 방장 전용 (0~99) |

### 티켓 & 이모지
| 명령어 | 설명 | 비고 |
| ----- | ----- | ----- |
| `/open` | 수동으로 티켓 채널 생성 | 일반 유저 가능 |
| `/close` | 현재 티켓 종료 버튼 출력 | 티켓 채널 전용 |
| `/answer` | 지정된 티켓 채널로 관리자 답변 송신 | 관리자 전용 |
| `/addemoji` | 이미지, URL, 기존 이모지로 신규 이모지 등록 | 지정 채널 전용 |
| `/delemoji` | 서버에 등록된 커스텀 이모지 삭제 | 관리자 전용 |

## 문제 해결 (Troubleshooting)
* **슬래시 명령어(`/`)가 보이지 않는 경우** : 
    * 봇을 서버에 초대할 때 `applications.commands` 스코프가 포함되었는지 확인하세요.
    * 봇 실행 후 Discord API 상에 슬래시 명령어가 반영되기까지 최대 몇 분이 소요될 수 있습니다.
* **`discord.errors.Forbidden: 403 Forbidden` 오류** :
    * 봇의 역할(Role) 순위가 제재 대상 유저보다 높게 위치해 있는지 확인하세요.
    * 봇에 해당 채널의 `메시지 관리` 및 `채널 관리` 권한이 부여되어 있는지 확인하세요.

## 문의 및 기여 (Contact & Contributing)
* 버그 제보 및 기능 제안은 [GitHub Issues](https://github.com/username/repo/issues)와 [서포트 서버](https://discord.gg/)를 이용해 주세요.
* 문의: [your_email@example.com](mailto:your_email@example.com)

## 라이선스 (License)
This project is licensed under the MIT License.