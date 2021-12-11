from testutil import table

def asserter(a, b):
  assert a == b

def test():
  table(asserter, 10, [(sample, 26397), (input, 339537)], [(sample, 288957), (input, 2412013412)])

sample = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''

input = '''([<{(<{(({<{{{[]<>}<<>()>}<<()()>[()()])}{({()[]}[<>{}])<(<><>)<[]{}>>}>{{((()<>)<[]()>)[{[]<>}(()[])]
<<[[<[(<[<[[[{()<>}(<>{})]]][{(<{}{}>(<>))[[<>](<><>)]}[({{}<>}<[]()>){<{}{}>[{}[]]}]]><{(<([][]
{<([[[({{(<[([{}<>]<{}{}>)[[<>[]]]]{{(()<>)[()]}}>){((([{}<>]{[]{}})<<[][]><<>{}>>){([[]{}]<<>()>){
{{[{({{(({<[<{[]{}](<>)>][<(()[])(()[])>[[<>{}](<>())]]><<([{}]{{}{}})[{[]}{{}[]}]>[{<()<>><<>>}]>
(<<<[(({[[[{<[{}<>]{<><>}><({})>}{{{()}{(){}}}}][{[({}{})[<><>]]<({}[])[()()]>}(<([]<>)<[](
<[{[((<<[[<[({[]()}{(){}})[{<>[]}<()()>]]>]]<[{{[[[][]]<[]()>][<<>{}><<><>>]}}({[<[]()><{}[]>]{<[]
(({((({{[[(([<[]<>>(())]{{()<>}<<>[]>}))]]([<([{{}()}(<>{})][({}<>)])>](({{<()<>>[{}())}{((){}){[]()}}})
({{({(<<{<<([<{}>])(<[()<>][{}[])>{[()()][{}{}]})>[[[{{}[]}[(){}]][{<>{}}{()<>}]]({<<>[]>{{
<[<<{[(<{[{({({}[])(()[])}[{{}<>}{{}<>}]){<{<>[]}[<>()]>{<{}()>}}}{{{{()()}}[{{}<>}({}<>)]}}}}>{{[[{<[
[{([<{{<<<[([<[]()>])]([{{<>{}}}{(()[])[<>[]]}])><[(<{()<>}{<>}>[([]{})<<>{}>]}([{()<>}({}[])]<<{}[]>({}{}
<([<([{{<<{<(([]<>)<{}{}>)>({[(){}]}((<>[])<{}[]>))}<{<(()[])<[]>>({[][]}(()[]))}(<{()[]}{[]()}})>>[([({()[
{{{[({(<[{[[{{()<>}[<>()]}{({}<>)<{}()>}]{{[()()][(){}]}[{<>()}]}]}]>)(({<<(({{}<>}([]<>))({<>[]}<[]{
({{({<([{[{{[[[]()><{}[]>]({{}[]}[{}()])}}<{[{[]()}[<>]]<[{}<>]<()<>>>}>]{<<(((){}){<>()})[[[][]]]>[([<><>]{
(<[[{{[(([{{<((){}){<>{}}>{<{}[]><<>[]>}}(({<>[]}<<><>>)({()[]}<()<>>))}<{(<()()>[{}{}]){{
{{{[{<<(<<[{({(){}}[{}{}])}[{[<>[]]{()()}}{[()]{(){}}}]]>>)><{((<<{<[]{}>([]{})}{{{}{}}}><([{}[]](()()))>
[<(<<<[(([((<<<><>>>[<[]<>>(()[])])[{((){}){<><>}}<<{}{}>(()[])>]){(([[]<>]<[]>)<{[]}[[]<>]>)<<{{}{}}[[
<(<<({(([[({[[[])(()[])][<[]()>{{}[]}]}{({{}}{(){}})(((){})([]<>))})([[([][])<{}<>>]<<()><<>()>>](
[{[[<{<<{<{<{<()()><{}[]>}([(){}](<>()))>(<{<>[]}([])><[[][]](<>{})>)}(({<[]<>>{()()}}<<[][]>>){({()[]
<([<{((({({[<(()[])[{}]>({[]()})]<<[[]]>>}<[[{[]{}}[{}{}]]([{}[]]{(){}})]({(<>())})>)}({<[{{{}
({{([(<<{({(<(<><>)<{}<>>><<{}()>[()()]>){<{{}()}(<>[]>>}})}>>[<<<{(({{}<>}(()[])){<[][]><{}>})
[<((<<{{<[[[[{[]()}][{[]{}}(<>())]]]]{<<{(()<>)((){})}<[<>[]]{[][]}>>(<(()())(()[])><{{}<>}({}())>)>[<<[(
[(<<(<<[(([{((()())<<><>>}[{()<>}({}<>)]}]{{<(<>[]){(){}}>([<>()]({}{}))}})<<(<[[][]][[][]]>[([][]){(){
<[([[<<[{(<([([]{}){{}<>}][{()}([][])])>)({<({(){}}){[[]{}][()()]}>{{{[]()}({}{})}(<[]{}><<>()>)}}[{[<[]()><
{<{<[[{({<[<<({})<()[]>>((<>{})<[]{}>)>]>})}((<[[(<<{}{}>{[][]}>)<<[()[]]{<>{}}>{{()[]}[()]}>]<({[
[({({(<<<<<[[<[]{}>]{<<>{}><[]{}>}]><<<([]{})<{}[]>><[{}[]][()<>]>>[[<{}[]>{[]}](<{}()>[{}<>])]>>>>{<{([((
<({[({<{[<({{<()[]]}[{()[]}[{}<>]]}{[{()<>}{<><>}]([[][]]<[]<>>)})>[[[(<()<>>({}[]))<[(){}]<<><>>>]][[<({}{}
{<(<<(([[{(<[[()[]]<()[]>]{<()<>><()[]>}><{<[]{}>{()()}}>)([([(){}]{<>{}})[{<>{}}[<>{}]]]<<[[]{}]{()
{[([[{[<[<{(<<[]{}]>({<><>}({})))([{{}<>}]<{()<>}[{}[]]>)}<([(()[])<()()>])<{{[]{}}[{}()]}(<<><>>[()()]
<<[{<[({((<<({{}()}{()[]})>[<<{}{}>{<><>}>]>){{<[{[]()}[[]()]]{[{}[]]}>[{<{}{}>{[]<>}}([{}[]]((){}))]}(
<<{((([[({<{[(()<>)<()[]>]({()[]}({}<>))}{{{[]<>}[{}[]]}[{<><>}]}>}<[[([{}()]{(){}})<({}<>)[[]()
{(([({{(([<{{{<>()}<<>()>}[{<>()}(()())]}>]{(<([()<>]{()<>}){{()<>}}><<{{}}{[][]}>(<(){}><{
{<(({{[<([(<<([][])(<>()]>{{{}{}}{[]<>}}>)[{(<()[]>{<>{}})[{()[]}<[]<>>]}{<{{}[]}><<{}>[{}<>
(<{{([<[[{{[{[[]()][()()]}{<<>{}>}][{{<>()}<()()>}(((){}){<>{}})]}{<(({}()))<[(){}]<(){}>>>(<({}[]>[[][]]>)}}
(({({[({<{{{[[()()]({}())]}[([{}]<{}()>)([{}()]{{}{}})]}[((<{}<>><()()>))]}[{{{(<>{}){<><>)}[<()()
(<({{<([{[([[({}<>)][([]<>){[]{}]]][[<()[]>]])][<{[[{}[]](())]<<()[]>(())>}{<{{}[]}[<>{}]>{<[]<>>
(([[([([<[{[(({}[])<[]{}>)]}][[{({()<>}[{}[]])(([]())(()<>))}<[<[]{}>({}<>)]{{{}{}}{[][]}}>]{{{
<[{[{<<{[[<{(({})(<>{}]){([]())[[]()]}}{(<()()>([]())){([]{})<[][]>}}>]{({[[<><>]{[]()}](<{}[]><[]<>>)}
([{<({{([([[{{()[]}}({(){}}[<>{}])>]({{(())([]<>)}<[()<>][[]()]>}([{()[]}{()()}])))](([[[{<>{}}[<>(
<[[[(<[{{[[{{{<>[]><<>>}[{()[]}({}())]}[<[{}<>]<[][]>>]]]}{{({{{<>()}{()<>}}<<{}[]>({}[])>}[[(<><
[[<[<({<[({{[[<>{}][[]{}]]{<()()>{<>{}}}}[<<<>{}><[]<>>><<{}<>>(()[])>]}){<[(([]())[<>()))[({}[])<
<<(<<<<((([[<<{}[]>(<>())>]]<{{[[]<>]<[]>}{[{}()]{<>[]}}}<[[<>{}]({}())]>>)){{([(({}[])({}[]
([{<([<[[[{[[{<>[]}{[]()}>([[]])]<({{}{}}({}[])){(<>{})<()()>}>}<{(([]()){()<>})[{<>{}}{<>()}]}<(([]
<{[<(({([[((((<>[])[[]{}])({[][]}))(<[()<>]{<><>}>)){<<{<>[]}<<>()}>>{({{}{}}(()()))}}]][{
({<{<<<{{{(((([]())[<>]){<(){}><{}[]>})<{([]<>)[<><>]}[{()<>}({}<>)]>){((<[]()>[<>{}]){<()<>>(
[{<(([(<[((([[(){}]{[]()}])))]>)[<{(<<[<<>[]><()()>]>>){[<{{(){}}({}[])}([{}()][<>])><((()<>)[[]])[[{}()](<>
{<<[<{[(<{<([{()[]}({}<>)]{[{}<>][{}()]})([{<>{}}<<>>])>{(<{{}())<{}()>>(({}[])<<>()>))[({<>()}[()[]])<<{}<>
[<([<<<[({([<<(){}><{}[]>>[[<>{}][{}<>]]]<[<()[]><(){}>]([<>{}][<>[]])>)<<{<[]<>>[[]{}]}<({}(
<[[(<[{[[({{{<<>[]][{}[]]}[[[]{}]]}}){{[[(<>{})(()<>)]({<>()})]({({}{})<[]{}>}[<()<>>])}{<{[()[]]}[<
<(<(<((<[((([[<>()]]){<[<>[]]><([]{})>})[<<{<>()}{{}<>}>(((){})[<>[]])>{[[<>()][{}[]]](([][])([]))}])((
[(<{{<(((<<{[[<>[]]]{([]<>)<{}[]>}}[<{{}{}}[{}()]><{[]()}[{}]>]>{[<{{}[]}([]<>)>[[(){}][()()]]]
<(<(([[{[<<<(({}))[{[][]}]>[[([]{})({}[])]]>[<<(<>[]){<>[]}><[()<>]>)<[{{}<>}(<>{})]{[<>()]{{}{}}}>]>{[{<{
({<({{{[[(([<<()[]><<><>>>])(<((<>()))(<<><>><[]<>>)>)){{({[[]()]{[]<>}}[[{}[]]<[]()>])}({({()()}<[]()
{{{<[<{<{[<(<{[]()}><[()[]]{[][]}>){<<[]>[<><>]>([<>()][<>()])}>)<<<(([]())[<>[]]){[[][]](<>{})}><([(){}]{{}{
<[((<<<({<[((<{}<>>[[]{}})((<>[])))({<()()>{<><>}}{(<><>){(){}}})][[<<[]>>[{<>[]}{[]()}]]([{
(((<<{<({<[[[{()()}(()<>))(<()[]>((){}))][{({}[])[{}()]}<<{}{}>{()()}>]]>})<<{{<[[<>{}]<[][]>]((<><
[<[{[[{{<{[(<<<>[]><{}()>>)({[{}[]]}((<>())<()[]]))]{{({()[]}([]<>)){{<>[]}[[][]]}}}}{({(<<>[]>{[]})[[{}
<<[({[[[[([<(<<>[]>{()[]})>{<[()<>]>[[[]<>]({})]}]<(<{{}}([])>[<{}()>])[{{<>()}<(){}>}<<<>{}}[{}{}]>]
([(((([[<[{({<{}>})<([{}<>][(){}])<<[]()><()[]>>>]{[([<>[]](()()))[{{}[]}[{}<>]]]({({}<>)[<>()]}<{()<>}{[]{
[[<{[{<{{(<(<[<>{}]><([]{})[{}<>]>)>{{[{<>[]}[{}()]]<<()>{[]}>}[[((){})([])]{<<>()>([][])}]})
{<[{{{<{([<[<{{}{}}[[]{}]><{{}[]}>]{(<{}<>><{}[]>)(<(){}><()()>)}>]<<<({{}}(<>()))[<{}[]>(<>{})]>({<[]>{()<
{<[{[<(({[{{({{}[]}[()[]]}}<(([]())[()[]]){(()){<>()}}>}[<<{<><>}>[([]{}){{}<>}]>[{{<>{}}{()[]}}
<{[{([<{<((<[<()[]>{[][]}]<<()[]><<>{}>>><([<><>]<()()>)({{}()}<(){}>)>){<(([][]){[][]})(<[]><{}{}>)>
(([<((((({{{[<()[]]{{}<>}]{<()()>({}<>)}}([[{}()]<<>>][((){})<<>[]>])}}(<{{[(){}]{()()}}}{([{}()
<<<((<[[{[<([<{}<>>(<><>)]<{[]<>}<[]<>>>)>]{([{[[]<>][<>()]}({[]<>}<<>[]>)])[[{{<>[]}(()())}
{<(<<<(({{(((([]<>)(<>[]))))}[(([[[][]][{}()]])<<(<>{}><{}{}>>{(()[])([]())}>)]}([({((<>){[]<>}){<[][]
({(([[[[<{[{(<{}[]>[{}<>])(<[]<>>({}[]))}{([<><>]{{}{}}){{{}[]}[[][]]}}]<[((()[])([]<>))[{[][]
[<([[([[<({({<[]()>}<[[]()]([]<>)>)([[()[]]]{[<>{}][()()]})))>]<({{[{<{}{}>}{{()()}[<>[]]}]{([{
({<<{{({[{[{{[[]<>]<(){}>}<<<>{}>({}{})>}<{[{}<>]}(<[]>[()[]]))]}]<<<<<{(){}}<<>[]>>{<[]{}>{(){}}
(({<([<((<((({{}[]}[[]()])){{[[]()]<[]{}>}(<[][]>{<>})})({{[()()]{{}<>}}(({}{})[<><>])}[[([]{})[
({{[(<{{<<<<[{{}{}}{{}{}}][<[]()>[[]()]]>([{{}}<[]<>>][<[]{}>{()<>}])>[<{({}{})({}<>>}[<{}<>>[<>()]]>]><<
{[((({{(<(<{[{[]()}}<<[][]>(<>[])>}<(<[]()><()<>>){[<><>]<<>()>}>><[{<()[]>}{[{}[]](<>{})}]>)<({<{<><>}>}{
[(([{([<<<([[(()())][([]{})[<>{}]]]({((){})((){})}(([][])[()<>])))[<((<>())[<>{}])>{{[[]<>](
<(({<([(<<<{([{}[]]<[]>)}({{<>{}}[[]{}]}(<{}[]>(()<>)))>>({<{<<>()>((){})}((()())[<>{}])><[<[]()>]{<
[<[{({<[({[(<[{}[]]{[]<>}>(({}{}){{}[]}))(<{()[]}>)]{<([[][]][{}<>])<<<>{}>>>{{((){}){()()}}<{{}}
[<([{<(<(<<{([[]<>]{(){}})((()<>)[[]])}<[<{}()>]<{<><>}<{}{}>>>>([{({}<>){{}()}}]<((()()))<<[][]>
({[{((<{[{([<{()()}{<>()}>[[()[]]]])}[{([[{}]{<>{}}]({[]()}[{}[]]))<{<{}<>>}>}]][[[(<({}{}){{}
[[<{{<{[([(<([[]<>][()<>]))[[[<>[]]]({()()}([][]))])(([[[][]]([]())])<{{{}<>}([]{})}<{[][]}{
<<({<[{[<{<<([<>()]({}<>))][([{}()][{}[]])]>}>]}{[<[[[[[[]{}]<{}>]<<{}()>{()[]}>]][<{({}())
(<<[({[([([[(<<>{}>){[(){}][()]}][[[(){}]{[]<>}]]]<[([<>[]]([]))[{{}<>}{()()}]]<[<{}[]>(()())]<<<><>>{{}[]
{([[[<[(<({<{{{}{}}[[]<>]}<[()[]]{<>[]}>>}<<<(()())<{}[]>>[([][])<<><>>]>[(((){})(()[])){<{}()>(()[])
{[<{[[[((<{[{[[]<>]{{}()}}[{{}<>}{<><>}]][<<()<>>{<>{}}>[{[]{}}((){})>]}(<[<[][]>({}())]<[<>[]](()[])
{({(<<{({({([<(){}>[()()]](<[]><[]<>>))([{<>()}<{}<>>]{<[]<>>[[][]]})})({[(([]<>)[[]])]{([[]{}]{{}()}
{{[<{<<{<{({(({}()))[<<>{}]{()()}]}({{[]{}}([][])}[<<>()>{[]<>}]))}>(<<[{<[]()><<>{}>}]{((<>[]))<(
{{[<[{<(([({([{}{}]({}[]))<<()>(<>[])>})[<<{[][]}<[]()>><{{}[]}<<>{}>>>{{{{}{}}{<>{}}}([{}
[[([(<{{[{{{{{()()}[[][]]}([{}()](<>))}<{<<>[]>[{}[]]}<<{}()>>>}}]<<[{[<{}>({})](<()[]>)}](<<<[][]>(
{<[([{{{((<{((<>())){<[]<>>}}<<{<><>}[<>{}]>{{()[]}(()[])}>>{{{<()()>[[]{}]}[[<><>]<[]()>]}([{{}}{()()}][(<>[
[{<{[([((<(<(((){})[<>]){({}[])<{}<>>}>(((()())([]{}))<[()()]{[]{}}>))([((()<>)<{}()})<{{}[]}<<>
{(({{{<[<({([<{}()>]{<<><>>{<><>}})}){<(((<>[])<[][]>)(<[]<>>{{}<>}))(<{<>{}}<()[]>>[[{}[]]({}())])>
{<([{(<{<<{(<{()}{<>[]}>)([[{}()]{<>{}}]<({}{})>)}[<<<()[]>({}<>)>[<[]>[<>{}]]><(<{}()>[<>{}])>]
<{{{{(({{{[{<[[][]]<()<>>>}[({{}[]}([]<>))({{}{}}{<>()>)]]}}}([{<{{<{}<>><<><>>}}{([{}<>]<<>{}>)
{<[<<{<([[[[[[<>[]](()[])]({{}[]}<{}>)][((()())({}()))<{{}[]}(<>())>]]([<[{}[]][<>[]]>]<{([]{})}{(
{<{[[([<([[[(<()()>({}[]))[{()[]}]]((({}[]><()()>)[({}){[]<>}])]]{<<{<()[]>}{<<>[]>{<>()}}>><[{(()<>)({}<
[[<[[<{{{{<<{{[][]}<(){}>}><{([]())[[]<>]}<<{}[]>(<>())>>>}<{{[[(){}]<<>()>]<{{}()}[[][]]>}}<(<<(
<[[(({({(({{{([]{}){<>{}}}{[<><>]{[]<>}}}}))[({[[({}<>){<><>}]{<<>{}><<><>>}]}[<{<{}<>>(<>{})}(([
({<<([{[<[<([((){})([]())][(()<>)({}[])]){{[{}()]({}[])}[{{}()}{{}()}]}>{{({<>[]}{<>})[<(){}>
<(<{<[<{({{[<{{}[]}{[]<>)>][{[{}{}][()<>]}(<[]<>>[[]{}])]}(([[[]<>]{()()}]<[{}[]]{<>{}}>)((([][]))
<{<(<<((<<[[{<()()><<><>>}<(()<>)({}<>)>>[<<[][]>(<><>)>{(<>[])}]](<{<()[]>([]())}[{<><>}<{}[]>]>)>>{(
{(({(<(<<[[[{<<>()><{}()>}[[<><>]{()<>>]]{[{(){}}]}]]>>)(<<(<({([]())<<><>>}({[]()}({}<>)))>
<{<<[<<{[<([[(()())<<><>>][<<>[]>(<>())]]({<{}{}><<><>>}{[{}]<<>[]>})){[{{[]}<{}[]>}[[(){}]{[]<>}]]
({[[{<[([[[{[[(){}]{[][]}]<({}[])({}())>}{{<()[]>{<><>}}<{<>}>}]{<<<()<>]{<>{}}>[<[]<>>{{}()}]><[<<
<{{{([({<{{([{()}[()<>]][(<>())(())])([({}[])[{}{}]]({{}{})([]())))}{(<[<>()]{()<>}><[()<>][<>[]]
((<[(<[(({{(<<(){}>{(){}}>({()[]}[<>[]]))<(((){})({}()))<<[]{}><()[]>>>}})<[{([<<>{}>]){<{<>{}}{()<>}>}}{{('''