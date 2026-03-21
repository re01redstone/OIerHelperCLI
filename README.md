# OIerHelperCLI
A CLI tool to help OIer to simplify the compile&amp;test process in terminal

### Usage
```bash
python3 OI.py [-h] [-i] [-c] [-p] [-a] [-j] [-s] file
```
#### Args
  file           input program name

#### Options
  -h, --help     show this help message and exit
  -i, --input    edit input file
  -c, --compile  compile
  -p, --run      run the test file
  -a, --answer   edit answer file
  -j, --judge    judge(compare) the output and answer
  -s, --strict   judge(compare) the output and answer strictly
#### Example
```bash
python3 OI.py T1 -icp # Edit the input file T1.in, auto compile&run the T1.cpp
python3 OI.py T2 -pa # Edit the answer file T2.ans, auto run&judge the T2.cpp
```
#### What is the difference between `-j`&`-s`
- `-j`, compare each segment(ignore empty space&enter) of the answer file & output
- `-s`, compare each line(ignore empty enter) of the answer file & output
