import argparse
import os,subprocess

def compare(out,ans,strict):
    out_lines=out.split("\n")
    out_segments=[]
    for line in out_lines:
        for segment in line.split(" "):
            if segment=="":
                continue
            out_segments.append(segment)
    ans_lines=ans.split("\n")
    ans_segments=[]
    for line in ans_lines:
        for segment in line.split(" "):
            if segment=="":
                continue
            ans_segments.append(segment)
    if strict:
        if out_lines==ans_lines:
            return True
        else:
            return False
    else:
        if out_segments==ans_segments:
            return True
        return False
            

def main():
    parser=argparse.ArgumentParser(
        description='Auto test the OI program',
        epilog="usage: python3 OI.py program.cpp -[cpih]"
    )

    parser.add_argument('file', help='input program name')
    parser.add_argument('-i','--input', action='store_true', help='edit input file')
    parser.add_argument('-c','--compile', action='store_true', help='compile') 
    parser.add_argument('-p','--run', action='store_true', help='run the test file')
    parser.add_argument('-a','--answer', action='store_true', help='edit answer file')
    parser.add_argument('-j','--judge', action='store_true', help='judge(compare) the output and answer')
    parser.add_argument('-s','--strict', action='store_true', help='judge(compare) the output and answer strictly')

    args = parser.parse_args()
    path=os.getcwd()
    file_in=os.path.join(path,args.file+".in")
    file_ans=os.path.join(path,args.file+".ans")
    file_cpp=os.path.join(path,args.file+".cpp")
    file_exec=os.path.join(path,args.file)
    if args.input:
        os.system(f'nvim "{file_in}"')
    if args.answer:
        os.system(f'nvim "{file_ans}"')
    if args.compile:
        os.system(f'g++-14 -O2 -lm -DONLINE_JUDGE -std=c++14 "{file_cpp}" -o "{file_exec}"')
    if args.run:
        result=subprocess.run(
            f'"{file_exec}" < "{file_in}"',
            shell=True,
            capture_output=True,
            text=True,
            encoding='utf-8'
        )

        print("-------OUTPUT-------")
        print(result.stdout)
        if result.stderr:
            print("-------ERROR-------")
            print(result.stderr)
        print("Return code:",result.returncode)
        if args.answer or args.judge or args.strict:
            f=open(file_ans, 'r')
            ans=f.read()
            if compare(result.stdout,ans,args.strict):
                print("Correct Answer")
            else:
                print("Wrong Answer")
            f.close()
        


    

        
    """
    TODO
    1√. 当输入-i时, 创建样例文件并打开
    2√. 当输入-c时, 编译
    3√. 当输入-p时, 执行样例文件
    4√. 按i/c/p的顺序执行
    5√. 比对文本, 开启时nvim xxx.ans, 比对输出
    6√. compare的严格(匹配每行内容)/宽松(匹配每段内容)模式
    """

if __name__=='__main__':
    main()
