#   https://leetcode.com/problems/remove-k-digits

#   https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3328

#   https://leetcode.com/problems/remove-k-digits/discuss/629860/Java-or-C%2B%2B-or-Python3-or-easy-explanation


class Solution:
    #   Wrong Answer
    def removeKdigits0(self, num: str, k: int) -> str:
        if not (0 <= len(num) < 10002) or not (len(num) >= k):
            return ''
        if len(num) <= k:
            return '0'
        nums = list(num)
        while 1 < len(nums) and 0 < k:
            if nums[1] == '0':
                nums.pop(0)
                while 0 < len(nums) and nums[0] == '0':
                    nums.pop(0)
            else:
                if nums[0] > nums[1]:
                    nums.pop(0)
                else:
                    nums.pop(1)
            k -= 1
        if 0 == len(nums):
            return '0'
        return ''.join(nums)

    #   Wrong Answer
    def removeKdigits1(self, num: str, k: int) -> str:
        if not (0 <= len(num) < 10002) or not (len(num) >= k):
            return ''
        if len(num) <= k:
            return '0'
        nums = list(num)
        while 1 < len(nums) and 0 < k:
            i, numSet = 1, set([nums[0]])
            while i < len(nums) and (len(numSet) == 1 or (len(numSet) == 2 and nums[i] in numSet)):
                numSet.add(nums[i])
                i += 1
            if '0' in numSet:
                nums.pop(0)
                while 0 < len(nums) and '0' == nums[0]:
                    nums.pop(0)
            else:
                maxNum = max(numSet)
                idx = nums.index(maxNum)
                nums = nums[:idx] + nums[idx + 1:]
            k -= 1
        if 0 == len(nums):
            return '0'
        return ''.join(nums)

    #   runtime; 488ms, 8.62%
    #   memory; 14.1MB
    def removeKdigits(self, num: str, k: int) -> str:
        if not (0 <= len(num) < 10002) or not (len(num) >= k):
            return ''
        if len(num) <= k:
            return '0'
        nums = list(num)
        while 1 < len(nums) and 0 < k:
            if nums[1] == '0':
                nums.pop(0)
                while 0 < len(nums) and '0' == nums[0]:
                    nums.pop(0)
            else:
                i, maxNum, maxIdx = 1, nums[0], 0
                while i < len(nums) and nums[i - 1] <= nums[i]:
                    maxNum, maxIdx = nums[i], i
                    i += 1
                nums = nums[:maxIdx] + nums[maxIdx + 1:]
            k -= 1
        if 0 == len(nums):
            return '0'
        return ''.join(nums)


s = Solution()
data = [('1432219', 3, '1219'),
        ('1043229', 3, '229'),
        ('10200', 1, '200'),
        ('10', 2, '0'),
        ('112', 1, '11'),
        ('1432232432028024207000023072903719', 13, '2207000023072903719'),
        ("17837605025683516120010270503807569928178393773076879170028133735644386709353014199231161016834202821655655947833118094662725822436120397735236953596117990380023771485471207752920307347213671242946302334923503764912432055700309914206103364063868546679428867424925671680526032099860583026255808370544562607516226496473439016990783116948597588838766623253667716587248969590351938547681019783978607010026047562010092976543940682873432990239799550710461153834255732312639561941973686912576394182153793380462425867680992707616498637668115274622735232014853260668113966532173703357431717064856689072299136043201776374633287565311907763102068659145456425775667706742465636096265155225620954708476056834360598143586342230201494961702397022909032525343629831061617524029740549732503118933345637593796835637332517547616659271620123917033661075709601596433920904019940562966413498015263253249142412825157794131174843234468459564274711666179597226827742043712416260860523360910980162117319761001613862299171678360951481566308393036484294993901787894130680931001392000616157647580922439841639930904162442127357667509444631452654167932805427619703245736090536294399929041051371778987081544103794722729388147025080306048634204352473482999895880695647790099394685750968059138436333859732024082730171757660571291417595802305409511232107280448213305231165480398075725857285869998210576485402736425879821085397455562017695363008611558982531486316307465097064168168166658487815536600146283315932845982056278890298387993190330818638373231049780830487273494495335029446430418137643408205920403671258231653232452868714269651394810511710355175377713236438578488103279674195967173766888222940086768571098694600319211909009646094264194127478728305805103963363118964826504060523778271289321697631407503790325751472604195238993275828794013996415561711633048132362919494041488640824641701759738001999542383400962940779371630674046472217805733281151035235202637339708666251450365824897008345046128797810143547987725537060801315455310242100055510909582437698931846483850334421121656504109448458027054491452194125036640794632386363044064534526209022794927345007241843949295466782511131163396823234411657640301905427698838637464844079306709926504479099260924169350712712720553819346627883796715038983527530340835148588622349232098889287963947139438792860255800361338904357812805049008158576663902534879866214043875419939892408257016251187254008934698598094555334280108354961045166987293796437056093657085921743249861532319109419437313463601454403605310855068137894822433238101196348067857972033523106499492535265371355668317593253809469723649187871395394253313828229881100055840458109506522859083007555749510020539324201525847318258764241744156587587916714377617189650554205200096218783642014526134338625548275976534692156322174184289272908952122334334390125082872291718753462353778992786774061266911831163380010223375915147625186721428143918734271528992089669547753557524867193927678623941268765642835531001988613342728339311331436518008901359377528188091555667165266417369977002811666057760084806413986136142955417704207453395457085849860417144543268047259000869805774718905632560977276684469334513978119604880662824867922542277069650187907536528145007583985755581779397657302590781603186091466026695317699892800061246962271357097523840041719784246024157938017994672941138071283119018925067825102464940330960161330506221384470767498008661627388078032860624578288341792501317651352795562576787320849025876548083246080026991031428818934616860288500110530122181734886637210817930716000042033282434677770717688221570127426876756884593282789855645127710287875493065449484125332525782131194923568511998782394785359222944374990359783797996139565156258346668284750667262720017164331953013767319174332903409375014146170940331020158161413416544211410296656831930989378749277259506120863394516398950064571601120864889258970256452671929001756518355749330756989162858306247412160789811176833908729197312700383322749579081734158933041267270230742488610603238898184429599281054988693215966094926483539887796223426073619224164016983857092002203322490838731829975383191772629965699002089808277065674142649866975519862080958190965813467433266995054717084257310341562631107204258353763526033001150670276556008053925726003714053852379201689005206537898107672412863406165354165881794581222402538582394034531943020815806788262514740689040363624138226520225626498812324657465956707980223435355827008328686364511759137999992432999912615887188783463472696784850152944717971072372325001407826815116846814068164938384559303433563786604720728652964069219543873592482001130011436669968153526575222356340367930446960047089186383237087691173292317894861809186558447513467342530162674519674032938817977413616230200646275026145725771248771101275556770493483491542922960629663771245512153294273756271522457001681254659092059182767257308674731917534288876000412360218697010958796382933346522055342511614148908721687298687680706555074691413660641450287858205609079897932889031777686879863949345327919902067397819765566129976750303380498787919297271921563022485220955001386321156137980137964431420532100091395380169215990801030102864362960134313468010877408051734198181101299132707248664138432881249872937753968305146577312351767204170358253387343016295172655145067762158282895537348371904688117450437149681202603501499966279649186174569075973662595689049963796503295154234637886318255497798386504114827192388124335901553175429022938510761582165572277133387192097140927088073158233212599672424927033005320332908224369012492882677292068078799976838113404738896262019497467600014015840334011626700032955692951380739724530263568156856229694296836540211842790419939788353905940465982062254137716945498466221199464580602183146127653116830997363040267934939190525310881553801998634869803521157354862572840952731954076805371435269572781799087347101911930635321924463496679350913435036926716653842331164754250768169343307317778689350987152108621051503084340174600982159019989113081125135930500699750029303290887893589750803412732405083874566006144161734977355260360055058002950219463832766406627457901190761723134590621607883454625136242268922197535166589917201553215741674277432931515989494159382777819092745465469348486101737073281032485649812430434828681099196913301814075666989559974026924390457113955179033305255228898937893472451280502813810149678268880700275090241288033281713565538744548984708044669307636138539658308411024255472658166509096627084043863963566269356917082925983228550149613817244191112851646768205163795913726472355163060739849008478748873768487826246447612436198788626026798471324146594617864729680769128803883786079804675812194890341511688521119787448113127949963821662203643845899442779327148487492549352820964644888437248602540974133245104864009258559180767950503105775370075967755758924119376922693735976724812221179302456898301547602559894802734228541782364427985652310968812856027327383432048808918063964172938440700254071667847703340785843944322842358398810621024842970428964678231838016263710176582859692564550022753163270007492899186139106750344620730775583601603374404611656809556083380699544367815527400373922543500224676274705721502530305043990524412594915859412967077960374102421462025367043748500375724783021816724173527991660601203980715593127762298484821449016372463459938357071741386930866703123614474755510644794949697664270819109571552218800083702074930464244543518434093693787233756741508267220541219832506625757787633598049592230042522262884855819543264184646927099066732042350071149564197732730797613121766044265574636134331540956556007480432896467640904267127326748174824811836600458958156434979294114184118283865697635786772343126668725550962670658596370409520570167064084793707259676243534530952777396939001516895613080144376365203665945733092525665638709263997523400935006451569916203221018118195118889009988016413636294174997794369473615615088456274292111981368731662062475712657309653997977804286141809048069574055575781747164681937644075964228797016561469233065455586059679774742063676295499150812960172504742885572086409822936213457964839564259297121312008094505010430617177272778919073232250748359070544563380172629868353842681267214151593752755066118992780672758673104313983802272083618756278661365527182811526040228986185536362318883731408309039092154304305645013041423615994243737805212911832197589793506833333911463880571935453499466629584072391679149940058608693680756674643583052707123393099161580293933779867187365929811994039237233343422557099716130982798579019502794062413109579149167289883382979869839713817849548283343299912948453900904964446069369601008517232120867037708130205445863620493064655944305168021973101774860919602083858123402739198174526886146067444295776444151792570345120790838463184199980395050456882710537925467406244909145522670812586881979901743891395166912293647291941337440725073532127978368289056650308921614958265259339184282248796248190230190244454117800434040219221772477093568667425954772897015525925329399369704414646762663264843008004555243477131519410179413322104081534024570123200650250991978395787917569552359471594290878528609073068145628999809548286008220597759424658296432291306269900278304769982668646749833919620051711969969525005630565920616181128323653809356542688784636253939263984024338857946939995288757783429529516813603425593738374345551031750187179351207901647517582666572728307485039405285941187820800238594616356765869060405354162213789937424361309256900254240194404175625187259500384452438702613803115895256658215243828658189032004993771341735076887650932388555857497314283598969975768345808741424348410747441870231018072867757297983891684386331405143446009180071463306634941891149758334619330413314655390266243713829108044720274746674032683434818324505265633238071614625733619390693329124957209563676768325862379259859360142740898116587999275280302222309622738078719893335146904356355236313676319868460065296188299103715979790911555198715901140860511528358327056", 1, "1737605025683516120010270503807569928178393773076879170028133735644386709353014199231161016834202821655655947833118094662725822436120397735236953596117990380023771485471207752920307347213671242946302334923503764912432055700309914206103364063868546679428867424925671680526032099860583026255808370544562607516226496473439016990783116948597588838766623253667716587248969590351938547681019783978607010026047562010092976543940682873432990239799550710461153834255732312639561941973686912576394182153793380462425867680992707616498637668115274622735232014853260668113966532173703357431717064856689072299136043201776374633287565311907763102068659145456425775667706742465636096265155225620954708476056834360598143586342230201494961702397022909032525343629831061617524029740549732503118933345637593796835637332517547616659271620123917033661075709601596433920904019940562966413498015263253249142412825157794131174843234468459564274711666179597226827742043712416260860523360910980162117319761001613862299171678360951481566308393036484294993901787894130680931001392000616157647580922439841639930904162442127357667509444631452654167932805427619703245736090536294399929041051371778987081544103794722729388147025080306048634204352473482999895880695647790099394685750968059138436333859732024082730171757660571291417595802305409511232107280448213305231165480398075725857285869998210576485402736425879821085397455562017695363008611558982531486316307465097064168168166658487815536600146283315932845982056278890298387993190330818638373231049780830487273494495335029446430418137643408205920403671258231653232452868714269651394810511710355175377713236438578488103279674195967173766888222940086768571098694600319211909009646094264194127478728305805103963363118964826504060523778271289321697631407503790325751472604195238993275828794013996415561711633048132362919494041488640824641701759738001999542383400962940779371630674046472217805733281151035235202637339708666251450365824897008345046128797810143547987725537060801315455310242100055510909582437698931846483850334421121656504109448458027054491452194125036640794632386363044064534526209022794927345007241843949295466782511131163396823234411657640301905427698838637464844079306709926504479099260924169350712712720553819346627883796715038983527530340835148588622349232098889287963947139438792860255800361338904357812805049008158576663902534879866214043875419939892408257016251187254008934698598094555334280108354961045166987293796437056093657085921743249861532319109419437313463601454403605310855068137894822433238101196348067857972033523106499492535265371355668317593253809469723649187871395394253313828229881100055840458109506522859083007555749510020539324201525847318258764241744156587587916714377617189650554205200096218783642014526134338625548275976534692156322174184289272908952122334334390125082872291718753462353778992786774061266911831163380010223375915147625186721428143918734271528992089669547753557524867193927678623941268765642835531001988613342728339311331436518008901359377528188091555667165266417369977002811666057760084806413986136142955417704207453395457085849860417144543268047259000869805774718905632560977276684469334513978119604880662824867922542277069650187907536528145007583985755581779397657302590781603186091466026695317699892800061246962271357097523840041719784246024157938017994672941138071283119018925067825102464940330960161330506221384470767498008661627388078032860624578288341792501317651352795562576787320849025876548083246080026991031428818934616860288500110530122181734886637210817930716000042033282434677770717688221570127426876756884593282789855645127710287875493065449484125332525782131194923568511998782394785359222944374990359783797996139565156258346668284750667262720017164331953013767319174332903409375014146170940331020158161413416544211410296656831930989378749277259506120863394516398950064571601120864889258970256452671929001756518355749330756989162858306247412160789811176833908729197312700383322749579081734158933041267270230742488610603238898184429599281054988693215966094926483539887796223426073619224164016983857092002203322490838731829975383191772629965699002089808277065674142649866975519862080958190965813467433266995054717084257310341562631107204258353763526033001150670276556008053925726003714053852379201689005206537898107672412863406165354165881794581222402538582394034531943020815806788262514740689040363624138226520225626498812324657465956707980223435355827008328686364511759137999992432999912615887188783463472696784850152944717971072372325001407826815116846814068164938384559303433563786604720728652964069219543873592482001130011436669968153526575222356340367930446960047089186383237087691173292317894861809186558447513467342530162674519674032938817977413616230200646275026145725771248771101275556770493483491542922960629663771245512153294273756271522457001681254659092059182767257308674731917534288876000412360218697010958796382933346522055342511614148908721687298687680706555074691413660641450287858205609079897932889031777686879863949345327919902067397819765566129976750303380498787919297271921563022485220955001386321156137980137964431420532100091395380169215990801030102864362960134313468010877408051734198181101299132707248664138432881249872937753968305146577312351767204170358253387343016295172655145067762158282895537348371904688117450437149681202603501499966279649186174569075973662595689049963796503295154234637886318255497798386504114827192388124335901553175429022938510761582165572277133387192097140927088073158233212599672424927033005320332908224369012492882677292068078799976838113404738896262019497467600014015840334011626700032955692951380739724530263568156856229694296836540211842790419939788353905940465982062254137716945498466221199464580602183146127653116830997363040267934939190525310881553801998634869803521157354862572840952731954076805371435269572781799087347101911930635321924463496679350913435036926716653842331164754250768169343307317778689350987152108621051503084340174600982159019989113081125135930500699750029303290887893589750803412732405083874566006144161734977355260360055058002950219463832766406627457901190761723134590621607883454625136242268922197535166589917201553215741674277432931515989494159382777819092745465469348486101737073281032485649812430434828681099196913301814075666989559974026924390457113955179033305255228898937893472451280502813810149678268880700275090241288033281713565538744548984708044669307636138539658308411024255472658166509096627084043863963566269356917082925983228550149613817244191112851646768205163795913726472355163060739849008478748873768487826246447612436198788626026798471324146594617864729680769128803883786079804675812194890341511688521119787448113127949963821662203643845899442779327148487492549352820964644888437248602540974133245104864009258559180767950503105775370075967755758924119376922693735976724812221179302456898301547602559894802734228541782364427985652310968812856027327383432048808918063964172938440700254071667847703340785843944322842358398810621024842970428964678231838016263710176582859692564550022753163270007492899186139106750344620730775583601603374404611656809556083380699544367815527400373922543500224676274705721502530305043990524412594915859412967077960374102421462025367043748500375724783021816724173527991660601203980715593127762298484821449016372463459938357071741386930866703123614474755510644794949697664270819109571552218800083702074930464244543518434093693787233756741508267220541219832506625757787633598049592230042522262884855819543264184646927099066732042350071149564197732730797613121766044265574636134331540956556007480432896467640904267127326748174824811836600458958156434979294114184118283865697635786772343126668725550962670658596370409520570167064084793707259676243534530952777396939001516895613080144376365203665945733092525665638709263997523400935006451569916203221018118195118889009988016413636294174997794369473615615088456274292111981368731662062475712657309653997977804286141809048069574055575781747164681937644075964228797016561469233065455586059679774742063676295499150812960172504742885572086409822936213457964839564259297121312008094505010430617177272778919073232250748359070544563380172629868353842681267214151593752755066118992780672758673104313983802272083618756278661365527182811526040228986185536362318883731408309039092154304305645013041423615994243737805212911832197589793506833333911463880571935453499466629584072391679149940058608693680756674643583052707123393099161580293933779867187365929811994039237233343422557099716130982798579019502794062413109579149167289883382979869839713817849548283343299912948453900904964446069369601008517232120867037708130205445863620493064655944305168021973101774860919602083858123402739198174526886146067444295776444151792570345120790838463184199980395050456882710537925467406244909145522670812586881979901743891395166912293647291941337440725073532127978368289056650308921614958265259339184282248796248190230190244454117800434040219221772477093568667425954772897015525925329399369704414646762663264843008004555243477131519410179413322104081534024570123200650250991978395787917569552359471594290878528609073068145628999809548286008220597759424658296432291306269900278304769982668646749833919620051711969969525005630565920616181128323653809356542688784636253939263984024338857946939995288757783429529516813603425593738374345551031750187179351207901647517582666572728307485039405285941187820800238594616356765869060405354162213789937424361309256900254240194404175625187259500384452438702613803115895256658215243828658189032004993771341735076887650932388555857497314283598969975768345808741424348410747441870231018072867757297983891684386331405143446009180071463306634941891149758334619330413314655390266243713829108044720274746674032683434818324505265633238071614625733619390693329124957209563676768325862379259859360142740898116587999275280302222309622738078719893335146904356355236313676319868460065296188299103715979790911555198715901140860511528358327056"),
        ]
for num, k, expected in data:
    real = s.removeKdigits(num, k)
    if 25 < len(num):
        print(f'{num[:25]}... {k} expected {expected[:25]}... real {real[:25]}... result {expected == real}')
    else:
        print(f'{num} {k} expected {expected} real {real} result {expected == real}')
