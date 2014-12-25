#coding=utf-8

import os
import time



if not os.path.exists(target_dir):
	os.mkdir(target_dir)

source = ['/Users/Gaejuk2/Documents/InBox']
target_dir = '/Users/Gaejuk2/Documents/Backup'today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = raw_input('Enter a comment --> ')

## 입력받음 여부를 확인.
if len(comment) == 0: ## 아무것도 입력하지 않은 경우엔 아래 블럭 실행
	target = today + os.sep + now + '.zip' 
else: ## 무언가를 입력한 경우
	target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'
	## x.replace(a, b)는 변수 x에 입력된 문자열에서 a를 모두 b로 바꿔준다.
	## 이 프로그램이 실행되어 사용자가 공백 4칸을 입력하면 밑줄 4개(____)가 입력됨.
	## 헌데, 이 경우 User가 Comment를 입력할 때, <this is file>이라고 입력하면
	## 파일명은 <%H%M%S_this_is_file.zip>가 된다.

if not os.path.exists(today):
	os.mkdir(today)
	print 'Successfully created directory', today

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
	## zip 명령어 뒤에 붙은 <-알파벳>은 zip 명령어의 옵션이다.
	## -q 는 quiet의 줄임말로, 프로그램 실행시 처리과정을 출력하지 않는다.
	## -v 는 출력 단계를 지정케하여 프로그램이 실행될 때 단계별 처리 상황을 화면에 출력하게 한다.

## Running the Backup
print "Zip command is : "
print zip_command
print "Running :"
if os.system(zip_command) == 0:
	print 'Successful backup to', target
else:
	print 'Backup FAILED'
