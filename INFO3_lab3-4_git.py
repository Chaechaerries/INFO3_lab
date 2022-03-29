#git 접속
$ git config --global user.name "Chaechaerries"
$ git config --global user.email chochaeeun724@gmail.com

#잘 접속되었는지 확인
$ git config --list

#코드 업로드
$ git init                      # git에 올릴 환경 조성
$ git add .                     # "."은 전체를 의미. 파일 하나만 하고 싶으면, 파일 이름 적기
$ git commit -m"first commit"   # 파일 이름 부터 ex)"최종본."
$ git remote add origin 주소    # 파일과 github 연결고리 만들기
$ git remove -v                 # github 주소 뜨면 성공
$ git push origin master        # code 보내기 -> [new brance] 뜨면 성공

#추가 업로드
$ git add .                     # "."은 전체를 의미. 파일 하나만 하고 싶으면, 파일 이름 적기
$ git commit -m"first commit"
$ git STATUS                    # 추가 업로드 되었는지 확인
$ git push origin master