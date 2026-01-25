# Streamlit → FastAPI + React 마이그레이션 가이드

이 문서는 기존 Streamlit UI/기능을 FastAPI + React 구조로 옮기는 방법을 정리합니다.

## 1) UI 이관 원칙
- **Streamlit 화면 구조 → React Page/Component**로 분리합니다.
- **Streamlit에서 직접 호출하던 계산/분석 로직 → backend/core/services**로 이동합니다.
- **Streamlit에서 상태관리하던 값 → React state 또는 backend 저장소**로 변경합니다.

## 2) Streamlit UI → React 페이지 매핑

| Streamlit 파일 | 역할 | React 위치(추천) | 비고 |
| --- | --- | --- | --- |
| `ui/landing_ui.py` | 랜딩/홈 | `frontend/app/src/pages/Home.tsx` | 공통 헤더/히어로 섹션 분리 권장 |
| `ui/result_ui.py` | 결과 리포트 | `frontend/app/src/pages/Result.tsx` | 리포트 컴포넌트로 분리 |
| `ui/gseed_ui.py` | 인증/지표 | `frontend/app/src/features/reports` | 결과 화면 내 탭 구성 |
| `ui/planning_ui.py` | 계획/시나리오 | `frontend/app/src/features/simulation` | 시뮬레이션 단계별 컴포넌트 |
| `ui/service_intro_ui.py` | 서비스 소개 | `frontend/app/src/pages/Chat.tsx` 또는 `Home` 섹션 | 챗봇 소개 섹션으로 재구성 |
| `ui/contact_ui.py` | 문의/컨택트 | `frontend/app/src/components` | 공통 푸터/문의 컴포넌트 |

## 3) Streamlit 기능 → FastAPI 엔드포인트 매핑

| 기능 | Streamlit 연계 | FastAPI 라우트(현 구조) | 이동 위치 |
| --- | --- | --- | --- |
| 주소 → 좌표 변환 | `core/services` 호출 | `GET /api/v1/geocode` | `backend/core/services` + `backend/infra/http` |
| 건물 정보 조회 | `core/services` 호출 | `GET /api/v1/buildings` | `backend/core/data_access` |
| 시뮬레이션 실행 | `core/services` 호출 | `POST /api/v1/simulation` | `backend/core/services` |
| 리포트 생성 | `core/services` 호출 | `GET /api/v1/reports` | `backend/core/services` |
| 서비스 소개 챗봇 | Streamlit UI | `POST /api/v1/chat` | `backend/ai` (RAG/프롬프트) |

## 4) 마이그레이션 단계
1. **UI 분해**: Streamlit 페이지를 섹션/컴포넌트 단위로 쪼개어 React로 옮기기
2. **도메인 로직 이동**: `core/services`의 계산 로직을 FastAPI에서 호출하도록 분리
3. **API 연결**: React에서 `frontend/app/src/api`의 클라이언트로 FastAPI 호출
4. **챗봇 확장**: `backend/ai`에 RAG 파이프라인(ingestion/retriever/prompt)을 추가

## 5) 체크리스트
- [ ] 랜딩 UI 구성 요소를 React로 변환
- [ ] 시뮬레이션 입력/검증 로직을 API 호출로 전환
- [ ] 결과 리포트 데이터를 API 응답 기반으로 렌더링
- [ ] 챗봇 응답에 서비스 문서/FAQ 인용 추가
