#   https://leetcode.com/problems/repeated-substring-pattern

#   https://leetcode.com/problems/repeated-substring-pattern/discuss/94455/1-line-in-Python


from collections import defaultdict


class Solution:
    #   63.25%
    def repeatedSubstringPattern0(self, s):
        if s is None or len(s) <= 1:
            return False
        if 1 == len(set(s)):
            return True
        def numbers(n):
            res = set()
            if 0 == n % 2:
                s = n // 2
                e = 0
                while s >= e:
                    if 0 == n % s:
                        res.add(s)
                        e = n // s
                        if e < n:
                            res.add(e)
                    else:
                        e += 1
                    s -= 2
            else:
                s = 3
                e = n // 2
                while s < n and s < e:
                    if 0 == n % s:
                        res.add(s)
                        e = n // s
                        res.add(e)
                    else:
                        e -= 1
                    s += 2
            return list(res)
        nums = numbers(len(s))
        for num in nums:
            #print(num, s[:num] * (len(s) // num))
            if s[:num] * (len(s) // num) == s:
                return True
        return False

    #   Wrong Answer
    def repeatedSubstringPattern1(self, s: str) -> bool:
        idxDict = defaultdict(list)
        for i, c in enumerate(s):
            idxDict[c].append(i)
        for l in idxDict.values():
            if len(l) == 1:
                return False
        for c in s:
            l = idxDict[c]
            subStrLen, subStrs = l[1] - l[0], []
            for i in l:
                if i + subStrLen <= len(s):
                    subStrs.append(s[i:i + subStrLen])
            if s == ''.join(subStrs):
                return True
        return False

    #   Time Limit Exceeded
    def repeatedSubstringPattern2(self, s: str) -> bool:
        idxDict = defaultdict(list)
        for i, c in enumerate(s):
            idxDict[c].append(i)
        for l in idxDict.values():
            if len(l) == 1:
                return False
        for c in s:
            l = idxDict[c]
            for i in range(1, len(l)):
                subStrLen, subStrs = l[i] - l[0], []
                if len(s) % subStrLen != 0:
                    continue
                subStr = s[0:subStrLen]
                if s == subStr * (len(s) // subStrLen):
                    return True
        return False

    #   Time Limit Exceeded
    def repeatedSubstringPattern3(self, s: str) -> bool:
        idxDict = defaultdict(list)
        for i, c in enumerate(s):
            idxDict[c].append(i)
        for l in idxDict.values():
            if len(l) == 1:
                return False
        for c in s:
            l = idxDict[c]
            for i in range(len(l) - 1, 0, -1):
                subStrLen, subStrs = l[i] - l[0], []
                if len(s) % subStrLen != 0:
                    continue
                subStr = s[0:subStrLen]
                if s == subStr * (len(s) // subStrLen):
                    return True
        return False

    #   https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3447
    #   runtime; 56ms, 72.32%
    #   memory; 13.8MB, 85.17%
    def repeatedSubstringPattern(self, s: str) -> bool:
        lenS, splitNum = len(s), 2
        while splitNum <= lenS:
            if lenS % splitNum == 0:
                splitLen = lenS // splitNum
                subStr = s[:splitLen]
                if subStr * splitNum == s:
                    return True
            splitNum += 1
        return False


solution = Solution()
data = [('abab', True),
        ('aba', False),
        ('abcabcabcabc', True),
        ('abcabcabc', True),
        ('bb', True),
        ('ab', False),
        ('zzz', True),
        ('a', False),
        ('abaababaab', True),
        ('lrfkqyuqfjkxyqvnrtysfrzrmzlygfveulqfpdbhlqdqrrcrwdnxeuoqqeklaitgdphcspijthbsfyfvladzpbfudkklrwqaozmixrpifeffeclhbvfukbyeqfqojwtwosileeztxwjlkngbqqmbxqcqptkhhqrqdwfcayssyoqcjomwufbdfxudzhiftakczvhsybloetswcrfhpxprbsshsjxdfilebxwbctoayaxzfbjbkrxirimqpzwmshlpjhtazhbuxhwadlptoyeziwkmgsovqzgdixrpddzplcrwnqwqecyjyibfjykmjfqwltvzkqtpvolphckcyufdqmlglimklfzktgygdttnhcvpfdfbrpzlkvshwywshtdgmbqbkkxcvgumonmwvytbytnuqhmfjaqtgngcwkuzyamnerphfmwevhwlezohyeehbrcewjxvceziftiqtntfsrptugtiznorvonzjfeacgamayapwlmbzitzszhzkosvnknberbltlkggdgpljfisyltmmfvhybljvkypcflsaqevcijcyrgmqirzniaxakholawoydvchveigttxwpukzjfhxbrtspfttotafsngqvoijxuvqbztvaalsehzxbshnrvbykjqlrzzfmlvyoshiktodnsjjpqplciklzqrxloqxrudygjtyzleizmeainxslwhhjwslqendjvxjyghrveuvphknqtsdtwxcktmwwwsdthzmlmbhjkmouhpbqurqfxgqlojmwsomowsjvpvhznbsilhhdkbdxqgrgedpzchrgefeukmcowoeznwhpiiduxdnnlbnmyjyssbsococdzcuunkrfduvouaghhcyvmlkzaajpfpyljtyjjpyntsefxiswjutenuycpbcnmhfuqmmidmvknyxmywegmtunodvuzygvguxtrdsdfzfssmeluodjgdgzfmrazvndtaurdkugsbdpawxitivdubbqeonycaegxfjkklrfkraoheucsvpiteqrswgkaaaohxxzhqjtkqaqhkwberbpmglbjipnujywogwczlkyrdejaqufowbigrsnjniegvdvotugocedktcbbufnxorixibbdfrzuqsyrfqghoyqevcuanuujszitaoaowsxyglafbwzddoznrvjqeyqignpitruijvyllsibobjltusrypanvybsfrxtlfmpdidtyozoolzslgdgowijatklvjzscizrkupmsoxftumyxifyunxucubvkfctkqlroqgzjvjwzizppvsomflvioemycnphfjtbnwedtubynsbirepgcxfgsfomhvpmymkdohettyycsibbeaxniwjkfvabnrllkmaglythkglauzgkeulyrpaeurdvexqlwgakdtbihmfrjijanxkhrqdllecyhbsuxnlftmjcnyybwsjmajbwtuhkkiovytgaufpjlxiwbnzhybsxfmumbhkjqmdabmyulbrglwstjkoxbczkjhvhsgzvwiixxaobhfsopqnebmflcooetjizolqrmsxphqdgzdmqhoggvrvjqrpmxbhkkfgzzxjegsyovdrmwcjavpmshojzxaxnbiztkfomzdhujdmcyxdqteqjalgqgsomonvbreqqzzpwqlihdnvudvlznfhbaokxvcelykfhxbldylqqewdnjzrlbskqgfvnqlfvobeyolyyovviwhxfpbuiujlolnjldgvwxljboaypaotdzjxxrschmwrveliumzpnoieipogwilaswntywuegdgyethsrznlzrffmwdgxaigmxpyvyaqgaultodtlgzcyvfiykmkllfbzxqyhvizqmamjzlvvgoifltzywueypmabinmyappzaecvmxirqsmzcuiddymnlfuskiheknevxtehxtbthqkjvtfzddlgchxczohpyewfmufzazyxtqxcuwbrxpfymuvfvsyxrrcfuusicczaqhlswbzievijhrvdudvmaravupityzffecdksuxteeitxtgwdfuydrtbfypbnkcypqodxrrwikfuxwjhtujrliuaifppzvkmxyspwvpfyfpkvgthqqrmajxispjncxgviyuqavayvsvznmhskodmidajwlkfrimprrhenguipdghstyopbvuiqcoplvwduwmjpblqoafnxwgqtvwztjekxwnbcuggliiehimvoymyjasinwspsqiukflhyfacamqrbqrypstsxhplrrmbeddvphnegtuxxtalsyxezjwtlwmxvrjtxytykkckuvbhhlovgcxjxhhivxnutkxvhadiaysulvknmcanhsyxlivarjdkgfcfpotnvlcibpxkidmwexpugwoxjicdkvstltienwqngiutnuqbzicontzlybgvumnwehjxoswnprlhvsuzvgyeettenngipfvrflpprjjalchhhcmhxkupciulccqssaqgdttpldmzdzveslyjadswtsbhgkddeouxbldsxzmfvhtonlampljgzyvemxhnlcrldtfthulkxhflcoupgeikrlaksuyfqvnvtnqspyjbxrnphouoyhvlswvoibuvbhhjcdflvlxrgorfbjrofokggafxmdqhqatsfezchpicyuawpovmmyzwforhkoatppybfofhdzsbiyjldsklgznfnqydisnyxzfpoftcjuprwygsnxkikqlimalfgxnuohrnhgqpublurhztntgmimcozuufzphdyiucrmmmjqtceykwnnbqorghzyzzukjqsjbmpfmdtrgvwvyeikgjdnmlxkxwldnmizapzuhsbssaxjutkbkoljyodlipofvnkqkktwtjlvgmkgjwlectlagylwdvomtuypjbtvitkqnnvtdxwrclpspcngrdrlsvyxfeohtupjvmyctacnifdnoryahqghzhoqprgkymyphiuvdvgjppfdgpouzjwbqkhqoyefmugjvewhxusqfzwuweifnsbijkeepyxrysojacqthkcijbzpmqfbmnrhybaibmzonzqlnmdjsvofgjftyfehikljfrfgznuaytvaegmaaljhrxtodjqxogwaxrssjxgvnkawzaqswwofedxjflugpktauixpzdckodknlbvxrsrjeobuvvqythyvzxbcgrlbgchwcperpbaxqbujxcxcklrrklkbnwlrwyuygzmgbyyhgapxwdbycdunhtedgvsrhchoxqwrssuhesetvejonqwhkwezjvjggmsqqyrxtjkcalswqqhvyimheopjzdkmouegzbphmgoxqwlbdlcumdgixjbcqvztzdjqmadthtdmvaqcagsyqggcfiifcoktjpjxcjyiwchyicqibxdgkqtgqiwpdklhumzwljmgdmicmunnnpdbamofynykqvsijsnfkpfyptlmqpoyjmeqvhcrvgmqmqopusqktdthpvztfzxrnqbsqtipqonxtsnasonzvxbpipyhhbtopsuqomfjrdyislifqgbndakaqbbwnkxnwpzeoohlxuhrtbfnqorfguvomeepxoffghmatidzfpfnwbfujdonlvyvwcwcchvsasdylbrrxfcztzqopdihybrhodjnmoqkijywkoncvrjozdphbfaalexgtpdtkzvsebevsopjvciwljfkrcumyacqdapwczenvmabkapuoudipbozezeygljfftvycbvazmzbndlfvlsqiaixdtbhqvlzdmffjfbfsvthrfmkoxbhokcvethucgqyvopafyttrhesvlbgihetenaiqyufxffdwqvruhvuzxukffmudygjavemzdccamymhppwofwgjkykmqfbuujzxhlnckmmcuflzandlltowjpwsaljtfapfvrmezbsjxsswiwjscisoqlhahzaplclkwlrgcdqbcdwbwafgadgtcpgowefkaqjuffuguqepwnfhbnbuinlicpdxfesoxcfqclfnrhgsxkhxgxrcorfygjxpiqmwtqjwbhghmlocnfkglorkkvxznlzdhucvayrzfazefobxutitrfkrlrstkcbtikklmhmggklsbphcejuylhxnraoenhdpzngyodiqlchxyycxzrrbhfwohfvxkrzolrglgnvcpjesdzygyoifoygphqqevqjugiuahmvrxgaujnyclcjqxevhyfnlohavrjlbyyvhghxhywekedhvwytysljsqminajfipdsprglnpxfqwuvcibpynkxgxsupmbntqrlwyampdgunigxldhlhqdyjcfhuqjfymrbafmyocttyjmnhlfnrtzddlazixtlxyvmvfbiguhsfuqoerhymsnoprkbdlchswocbbwwdvastaiamnepwkyaqmpliruphedkxjqzgpexlwulswtvotlgotlncpvnrrzerzdygeraoozbttnyyifkindeouuagqgztvqdolfrzrlzddjzcshvdgkhxkdxflwxmejkkszylbhoaacicwqiizickgcdxstpzkskjwdqegrearjrncmmkdelekbesuhquepjrnrzbllldgdmyrpglrhllwnqozfudjpchowhwevbqvjjezsmhylnjpktbspxnktxkmcfxwiaqqbhqjwufmwresfsfaokeaaadziobioqmtsvjgzkgkhbzpaeuexyudhrioicyqsjmngrwqpoherwuvdgeruffmlgphwbxzovyewtfazfpmvfvyguqditjlxnoixsyghyfrdngjfblyveibcapetpmeaidrtpnwwiifhpfgsptkvhhwkzvtvlhhbipjxurgqbtldimsarncplkeweoirjenakyprzzphewoprwyvfpjyglzrmhfqpdubheeqtgrmbxlcmnbtaqakgimuapsbuxzokhwnykughmwrlkjsvtdlzwpbhcsbvjnomutffmjggrmyilgschgwrrztnmvndmuahvnlwpwtglvbtkegzjstpiwllpgnlpcnezqscxkelindfvurtxsezrwzvzechocnvfaimxrqnyiqlybugjsblhzfravznkbtgcpqwovwpxzgxgodlhmixisfzdknoxzasscewgzvqkxuqrsqxsfwdwneyqisozqjfgrvhfsfeuspujvqhydwveadosqafyxbmzgrotyffqblolplosqnfcwxiuwkldpuenodlvotbqiizudxqjvfnkyicjcywjkfvukvveqhjrxdcigwbjdftdyelydzyummmtzuvfmaicednymxoaiuhigfkfavgeemcgofnaefganqoniqebfibigljbceulicojzjfrceigxprunjncymbrljfqmwciqtyncafzjyagimmzuejrttefhdwqcizyiurxvfbwrjxffzbjexshvwrxwrmhrbdxjwipsdfhtknfaswfrvxqdkhbwwefbvqsghhhutdgethcwupzrtsbhbjnbqwpccoaonxwvkhowbzhaoscgykzbiltlwqqatyeczzceuuwgvjxzonhkkfjcbwsezdmifdegsyjtswselknxweimxlnzohgtqthlftjblnphtdwwvsscbhjmruuqscwjpynxbkoomwdecqkrtbxgzgcxhppcjnqtcfqttkkolzcfikwblxkimijeglxsvcrkcqjjwcwuhvzydmegubqavlqffhrzzrhiwxrgftittdxcaybczncsyjlzlxyyklcppoxcgnexmaajzuhabdhaccuualacylsmtkewbprsmoncggqvrvsqqoffmwkplsgbrpurgioajuppvqluhbdetzdzwwzaelmopafumtqugecywglucmugwqiizveswrjevfzdnxlbkakrpzcejvxzeoybbtfdsvewjsivwswzjhudtpqsfclzcmukotirrxxtzksmxnjumofzhhowyftzfzbotrokaxaryxlkmueolqkrdxmzhoqnzvudeowcjloesfmqgvxwfyhnpbepbvbgjtbvqpoeugoqynkbfivmfewjjscjreixyqssxzsydgllfzmobnurxkwcypctjkabigwqtldwhjouaswtovdtkrlonzgeyddkqwuhnimzffxviyvsktqrfafqujhdepvczzhiyjlkxmeplnrvxgshdykehkefpkvepcxhozpjxtreynyliguhuxudbnhmfojordxzmmklgohcmmbukzshyrmooliaobbnlapadutnbetocxylceyxywdsjegdfcrsblbxhjsgcuoxmqftytngzdcmsrfyjjumcbxoleldazwzwtdjoyuqeqjfxazjarqgfmsfxyfqbeoktcctnfqrsjchxpqiltaqzawhguusgenjcfxriyfikpgdvwhbyumthkiktbecjwalsxqjyajrkcvysicisabtbrdeumbvtviihjwxdczpdnrrgmemxydgxlrjzucxyidwcdvdpvjlagwmgcngnpxjkximsogvyhnchlimsxcjwtrijtizpezjlcqekojrrjzvtvhnqvieqmdiedzqswrsnfmnneltcutqfcqyrrwmnwtelvsqrruwfjwrhjcrtbcytnyqmqxceuohpiffaqnrmoybqjjgdyotpmxttqftypfexlvdtgxqafiqbqjlnpbflkgaynkddbzllecdctccvslpdcurkxfoimnwdfvnyqkzlheruxrmiiygnzfovnrwcoqsgoameiunvzemmxtklistlxuynrwsjaxzwmhktdayzzoxbbemejgosgcynfapykbcnzhesvnctfvdspqkuyrjhykpadahbhjbatvsxlngbtxmqrbwqromfqzyabzrcoorbbyklndcqdjzcnsmgmwmpbgjqoykrvnafhqrwfajnfahyqocdbgfnlaozmffvvmoymbmytjvfcgttcijyyljdgwjbztlpswmalgbgpaplqgzqchflxtypttkrpfvxrtkzpzrscwbxqbwfqqvjcukjbsginxqmxryxieyavnzdiludhthpreyelgcnpsoqswsreogbmveofvusdsxcjvdrjkhxkqrqzjbrpljwuzplxczqeevvbvcwhnvzuszqvhlmaptylyufqzyldwwgezlqurzvorxwgdtgjilgydqvpkntwjbgihlwckorgrmxixylxjmlfvhbpoaboylcedyzeayigfagitkrextlipvqqhdmoerchoqxbypihdvpdtjrrkxroowtrexuhucxpiibvmuyarjwqpcoywawqwdmfpwvamisnskbhopoqdsrefjtmnmvkyccremktrniqwoofoeenbzvvlrfcsftapyujmwdupdqikocrdyexjbcxwqeaumqoklsqebuzeziiswzfzgyhvnwjcnshdybjywyaodsywmlmuueocfruntpztlbggsuzctocyilfzpszgrgjsimqypqopfumpmsjvmsbrcfwretbiekoxpmplpcgewmqigymreqevdydvgmuyytguexnycqhwialkbjgzcklmgxgijjyjlplrsxznfkoklxlvpxrbasbznvxasxztwnqbhqultkyfqxsaeqztxbuwpzdpkngnuoayckfykdlarmuwprgtghfxfbgpucqwbihemixqmypjedyedimaanpbdrxpvtoxmxzimgfaouzlteobnadoshnxnufgmypupeikfqrqyexoljhqsaneicvaerqxcngmsidszagpiuiiasrezakiuroadojxmvgqgdodwwjszyeruwnupqgmyrjxigaskpjmzpsbhgokwtfcisjzvepyebwrcpafxzhbdgjykhzemfomgxjphcscuxjnywoiwbdvusywqlsccvsropvrnxtmkgiwfvqfkotpdznjinpobubzbvstkkvubuucilxyhjbcilfldibmyebrlcnvnuuqfvhwxoorbyyiigppuftqswpksfdxicemjbftgoabwrqdoudfbyjutkeqakoarruhwuznnlydivfelxvtggkkkjmxlwbkbklbwfsvrbadvraqovanlsmklnfjxxvzdjlpyurxpjcssebtpznwoytjefobdynaiukctgrzjxzirzosjuncvhfhcnhhrajahitnbkvwtifcoqepqyzwyazzkddxywvgqxofsyxngevsdbatvzmziqpmjewiyorpzsupxoflqpbyzhtvvpjdcqnlvlzrzakvmxzbaeipmwouvpvgtekfkuajjogbxhjiiqisdbplotyakxjvkmxhtmyznhaylqjnqzrwrmgtumbbhflizbpeohsufreefajrcsfoghglucidbnlysamvyatutjdfnvhahxykurbrmmadeaxhghvfacnjxqjathltizloasimpzugutrjfozvgmdakdhaofiephsnuztnpqhdlfrfuyprcrcszmgplszwfndzihegtbxbspaucjbmsamjyqqraszaghzlgnfoasvljxltcnumquohlcgtfjmrmfccjrhfedlievtpieworwhyiucsetdtuquartspkotmxqpnkeluekveljyugrloqczljmwtmfkyvqguqquztpjidglpxqfxvhlftvvimvrozdyywopwyfovdzopwlumocnyuoumehvjqpzkcfcgihicdrdtttiixlhpikbvjgoblttgvmndkqggypgwsibcqahmyyeagklprtvojuwlcblwidhjpugkbuspeynaoocgkzrpcnbqajopjjlfthevbculqsozkndgojnjnxqsoqiazyesldujjlpeedrswybwlfyzphixzluwbtmoxokksbedrqfuizopajzeahvalehdfnrkmnlpimduzgmwszcxmracvelbhjzmiwdnxwruqcugmkscfodjxghwcbmsokdspilajnibphjrvvlwpbojlpwuytkosjjojczwonovrxsiyuidphsklrmialvzpjcjtpblsgqljhuuvkcgpopdruidbaguevssjulnqgsixuhdhffrizkwtcbmrsrmtinefwxwwilbezedywxuitdzyypdgoveeupeusrgkqwfslfnjlybghedeabnrlzcgflgxiftmfzcsnybqcegpxtepyifqblzdjrtynxjgbiymhjumliovwn', False),
        ]
for s, expected in data:
    real = solution.repeatedSubstringPattern(s)
    print('{}, expected {}, real {}, result {}'.format(s, expected, real, expected == real))
