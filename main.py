import argparse
import os,subprocess

EDITOR='nvim'
COMPILE_COMMAND='g++-14 -O2 -lm -DONLINE_JUDGE -std=c++14' 


def compare(out,ans,strict):
    # split the output
    out_lines=[]
    out_segments=[]
    for line in out.split("\n"):
        if line=="":
            continue
        out_lines.append(line)
        for segment in line.split(" "):
            if segment=="":
                continue
            out_segments.append(segment)
    # split the answer
    ans_lines=[]
    ans_segments=[]
    for line in ans.split("\n"):
        if line=="":
            continue
        ans_lines.append(line)
        for segment in line.split(" "):
            if segment=="":
                continue
            ans_segments.append(segment)
    # compare
    if strict:# strict, compare each line
        if out_lines==ans_lines:
            return True
        else:
            return False
    else:# normal, compare each segments
        if out_segments==ans_segments:
            return True
        return False
            

def main():
    # create parser
    parser=argparse.ArgumentParser(
        description='A CLI tool to help OIer to simplify the compile&amp;test process in terminal',
    )
    # args
    parser.add_argument('file', help='input program name')
    parser.add_argument('-i','--input', action='store_true', help='edit input file')
    parser.add_argument('-c','--compile', action='store_true', help='compile') 
    parser.add_argument('-p','--run', action='store_true', help='run the test file')
    parser.add_argument('-a','--answer', action='store_true', help='edit answer file')
    parser.add_argument('-j','--judge', action='store_true', help='judge(compare) the output and answer')
    parser.add_argument('-s','--strict', action='store_true', help='judge(compare) the output and answer strictly')

    args = parser.parse_args() # get args
    # get file name
    path=os.getcwd()
    file_in=os.path.join(path,args.file+".in")
    file_ans=os.path.join(path,args.file+".ans")
    file_cpp=os.path.join(path,args.file+".cpp")
    file_exec=os.path.join(path,args.file)
    
    # process
    if args.input:
        os.system(f'{EDITOR} "{file_in}"')
    if args.answer:
        os.system(f'{EDITOR} "{file_ans}"')
    if args.compile:
        os.system(f'{COMPILE_COMMAND} "{file_cpp}" -o "{file_exec}"')
    if args.run:
        # execute
        process=subprocess.Popen(
            f'stdbuf -oL "{file_exec}" < "{file_in}"',# disable buffer
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8'
        )

        # show the output
        print("-------OUTPUT-------")
        stdout=""
        for line in process.stdout:
            print(line,end="")
            stdout+=line

        # wait for return
        process.wait()
        print()

        # show err&return code
        if process.stderr.read():
            print("-------ERROR-------")
            print(process.stderr.read())
        print("Return code:",process.returncode)

        # judge
        if args.answer or args.judge or args.strict:
            f=open(file_ans, 'r')
            ans=f.read()
            if compare(stdout,ans,args.strict):
                print("Correct Answer")
            else:
                print("Wrong Answer")
            f.close()

if __name__=='__main__':
    main()
