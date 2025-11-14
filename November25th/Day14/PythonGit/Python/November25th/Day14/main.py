
#git 명령어 정리
'''
# Git 기본 설정
git config --global user.name "User Name"           
git config --global user.email "email@example.com" 
git config --list                                   


# Git 저장소 생성 & 복제
git init                                            # Git 초기화
git clone 주소.git                                   # 저장소 복제


# 브랜치
git branch                                          # 브랜치 목록
git checkout main                                   # main으로 이동
git branch -d old-branch                            # 브랜치 삭제
git checkout -b new-branch                          # 새 브랜치 생성 & 이동


# Git 상태 확인
git status                                          # 변경사항 확인


# 스테이징 (add)
git add file.txt                                    # 특정 파일 추가
git add .                                           # 전체 파일 추가


# 스테이징 취소
git reset HEAD file.txt                             # 스테이징 취소


# 커밋
git commit -m "커밋 메시지"                         # 커밋 생성
git commit --amend -m "수정된 메시지"               # 마지막 커밋 메시지 수정


# 원격 저장소(Remote)
git remote add origin 주소.git                      # 원격 저장소 추가
git remote -v                                       # 원격 저장소 확인
git remote remove origin                            # 원격 저장소 삭제


# Push (업로드)
git push -u origin main                             # 최초 push
git push                                            # 이후 push
git push -f                                         # 강제 push (주의)


# Pull (업데이트)
git pull                                            # 원격 저장소에서 업데이트 가져오기


# 로그(Log)
git log                                             # 전체 로그
git log --oneline                                   # 한 줄 로그


# 변경 비교(Diff)
git diff                                            # unstaged 변경 비교
git diff --staged                                   # staged 변경 비교


# 파일/폴더 삭제
git rm file.txt                                     # 파일 삭제
git commit -m "Remove file.txt"                     
git rm -r folder_name                               # 폴더 삭제
git commit -m "Remove folder"


# 파일 이름 변경
git mv oldname.txt newname.txt                      # 이름 변경
git commit -m "Rename file"


# Reset (되돌리기)
git reset --soft HEAD~1                             # 커밋만 취소 (변경 유지)
git reset --hard HEAD~1                             # 완전 되돌리기 (커밋+변경 삭제)


# 특정 버전 이동 / 복구
git checkout <commit_hash>                          # 특정 커밋 체크아웃
git reset --hard                                    # 작업 내용 완전 초기화
git clean -fd                                       # 추적되지 않은 파일/폴더 삭제
'''
print("Git 명령어 정리 완료")