import h3
h3_index = h3.geo_to_h3(40.2573225184, -74.7961659355, 10)
print(list(h3.k_ring(h3_index, 1)))
print(h3.h3_to_geo_boundary(h3_index, geo_json=False))

lst = [[-74.7961659355, 40.2573225184], [-74.7376353, 40.2096325996], [-74.7365560004, 40.2049442004], [-74.7385219074, 40.2022611843], [-74.7426864838, 40.2038359521], [-74.7446668987, 40.2066230058], [-74.7465944633, 40.1993091366], [-74.7480265061, 40.2104303162], [-74.7505364126, 40.2047297942], [-74.7504727864, 40.2002140791], [-74.7518840001, 40.1986588377], [-74.755661277, 40.2056889816], [-74.7576635025, 40.1976591962], [-74.7587885045, 40.2126131531], [-74.7615293049, 40.2074477068], [-74.761859907, 40.2043401875], [-74.734932536, 40.2169911691], [-74.7370159997, 40.2238808003], [-74.7425452787, 40.2295385842], [-74.7407666995, 40.2165242004], [-74.7414561954, 40.2121634917], [-74.7432870693, 40.2248157211], [-74.7423656535, 40.2198021342], [-74.748154744, 40.2156924937], [-74.7392115001, 40.2385422004], [-74.7416398003, 40.2329152998], [-74.7435337003, 40.2428287], [-74.7460721004, 40.2373463471], [-74.7521018624, 40.2435554], [-74.7496987996, 40.2293870998], [-74.7514298996, 40.2352332001], [-74.7512439996, 40.2239780002], [-74.7542796002, 40.2190475002], [-74.7539253887, 40.2105825681], [-74.7569956001, 40.2236366996], [-74.7584613215, 40.2298211467], [-74.7602839738, 40.2345399443], [-74.7615481001, 40.2277391], [-74.758984512, 40.2206847175], [-74.7638448998, 40.2147323998], [-74.7702942244, 40.2210936874], [-74.7732648922, 40.2241694689], [-74.7718024132, 40.235271129], [-74.7731734002, 40.2322579001], [-74.7773986004, 40.2295121996], [-74.778804303, 40.2370876168], [-74.7869060838, 40.2381973502], [-74.7916969269, 40.231672496], [-74.7932996941, 40.2422722129], [-74.7999188569, 40.2466836077], [-74.7896579151, 40.2522172286], [-74.7864479833, 40.2487596207], [-74.7802626865, 40.242385832], [-74.7745876733, 40.2381497606], [-74.7717776552, 40.2488241839], [-74.7617933974, 40.2451731526], [-74.7540253465, 40.2417532347], [-74.7813941689, 40.23214321892]]

lats = []
longs = []
for pair in lst:
    longs.append(pair[0])
    lats.append(pair[1])
print(min(lats), max(lats))
print(min(longs), max(longs))

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


polygon = Polygon([[-74.760851,40.199232],[-74.760897,40.199291],[-74.76092,40.199321],[-74.761285,40.199797],[-74.763436,40.202605],[-74.76427200000001,40.203563],[-74.766989,40.206674],[-74.76713599999999,40.206874],[-74.767275,40.207076],[-74.76740700000001,40.207282],[-74.767532,40.20749],[-74.76764900000001,40.207701],[-74.76767700000001,40.207752],[-74.767759,40.207914],[-74.767861,40.208129],[-74.767955,40.208347],[-74.76804199999999,40.208566],[-74.76812,40.208787],[-74.76814299999999,40.208857],[-74.768171,40.208949],[-74.768191,40.20901],[-74.768253,40.209234],[-74.768306,40.209475],[-74.768366,40.209714],[-74.768434,40.209953],[-74.76850899999999,40.21019],[-74.768574,40.210373],[-74.76858799999999,40.210412],[-74.768592,40.210426],[-74.76875200000001,40.210795],[-74.76891999999999,40.211162],[-74.769097,40.211526],[-74.769282,40.211888],[-74.769476,40.212247],[-74.769678,40.212604],[-74.76988900000001,40.212957],[-74.77010799999999,40.213308],[-74.770336,40.213656],[-74.770571,40.214],[-74.770872,40.214404],[-74.77099200000001,40.214574],[-74.77111499999999,40.214742],[-74.771242,40.214908],[-74.771293,40.214973],[-74.771338,40.215039],[-74.771377,40.215108],[-74.771404,40.215144],[-74.77143700000001,40.215176],[-74.771477,40.215205],[-74.77152100000001,40.215228],[-74.771569,40.215247],[-74.77162,40.21526],[-74.771719,40.215287],[-74.771816,40.215319],[-74.77191000000001,40.215356],[-74.772251,40.215502],[-74.772358,40.215544],[-74.77246,40.21559],[-74.772558,40.215642],[-74.772651,40.215699],[-74.772738,40.215761],[-74.77282,40.215827],[-74.773347,40.216256],[-74.773425,40.216323],[-74.77350800000001,40.216387],[-74.773595,40.216447],[-74.773658,40.216502],[-74.773715,40.216561],[-74.773765,40.216623],[-74.773808,40.216688],[-74.77384499999999,40.216756],[-74.77387400000001,40.216825],[-74.77389599999999,40.216896],[-74.773928,40.216953],[-74.773966,40.217007],[-74.77401,40.217058],[-74.777491,40.219213],[-74.777805,40.219408],[-74.778302,40.219714],[-74.778355,40.219747],[-74.781206,40.221508],[-74.781257,40.221537],[-74.78163600000001,40.221756],[-74.781943,40.221933],[-74.78201300000001,40.221973],[-74.78227699999999,40.222126],[-74.78254,40.222277],[-74.783276,40.222702],[-74.783508,40.222836],[-74.78401100000001,40.223126],[-74.784126,40.223192],[-74.78424099999999,40.223258],[-74.78433200000001,40.22331],[-74.78442099999999,40.223362],[-74.78503499999999,40.223716],[-74.78564799999999,40.22407],[-74.785972,40.224258],[-74.786169,40.224372],[-74.78668999999999,40.224673],[-74.786964,40.22483],[-74.78706,40.224885],[-74.787143,40.224933],[-74.787153,40.224939],[-74.787204,40.224969],[-74.787238,40.224988],[-74.787389,40.225075],[-74.788023,40.225441],[-74.78880700000001,40.225893],[-74.788906,40.22595],[-74.789006,40.226008],[-74.789108,40.226064],[-74.789134,40.226078],[-74.789231,40.22613],[-74.78926300000001,40.226147],[-74.78938100000001,40.226211],[-74.789647,40.226354],[-74.78971300000001,40.226389],[-74.78973999999999,40.226404],[-74.79003299999999,40.226562],[-74.790803,40.226978],[-74.790891,40.227026],[-74.79097899999999,40.227073],[-74.792241,40.227754],[-74.79246000000001,40.227872],[-74.793142,40.22824],[-74.795306,40.229408],[-74.795344,40.229423],[-74.795382,40.229438],[-74.79730600000001,40.230208],[-74.801203,40.231786],[-74.805207,40.233408],[-74.809207,40.234768],[-74.81020700000001,40.235108],[-74.81061699999999,40.235258],[-74.810779,40.235317],[-74.811072,40.235424],[-74.81169800000001,40.235654],[-74.81187,40.235717],[-74.811914,40.235733],[-74.812749,40.236039],[-74.813188,40.2362],[-74.814178,40.23656],[-74.815167,40.236921],[-74.81572199999999,40.237124],[-74.816171,40.237288],[-74.81733699999999,40.237714],[-74.817909,40.237924],[-74.81887399999999,40.238276],[-74.81903200000001,40.238334],[-74.818352,40.239385],[-74.817457,40.240791],[-74.817368,40.240944],[-74.81730399999999,40.241047],[-74.81723,40.241164],[-74.816546,40.24226],[-74.816135,40.242891],[-74.815906,40.243244],[-74.81587500000001,40.243287],[-74.815854,40.243336],[-74.815792,40.243313],[-74.81569500000001,40.243273],[-74.815646,40.243255],[-74.815442,40.243191],[-74.814956,40.243038],[-74.81228,40.242199],[-74.81097800000001,40.241774],[-74.810513,40.241617],[-74.810474,40.241669],[-74.81017199999999,40.242076],[-74.81008799999999,40.242188],[-74.809527,40.242945],[-74.808954,40.243952],[-74.808727,40.24436],[-74.80868100000001,40.244432],[-74.80625000000001,40.246126],[-74.80558000000001,40.246596],[-74.805556,40.246613],[-74.80538,40.246738],[-74.803347,40.24815],[-74.802891,40.248467],[-74.80262999999999,40.248317],[-74.80259700000001,40.248298],[-74.80235500000001,40.248155],[-74.801473,40.247633],[-74.800843,40.247281],[-74.80068900000001,40.247181],[-74.80062700000001,40.247317],[-74.800505,40.247245],[-74.800331,40.247144],[-74.798857,40.246279],[-74.79855000000001,40.2461],[-74.798545,40.246113],[-74.796952,40.24517],[-74.796166,40.244679],[-74.796088,40.244645],[-74.79534099999999,40.245306],[-74.79400200000001,40.246491],[-74.793798,40.246672],[-74.793245,40.246337],[-74.791849,40.245493],[-74.791809,40.245586],[-74.790122,40.24503],[-74.790009,40.245315],[-74.789621,40.246312],[-74.789227,40.245903],[-74.78858099999999,40.245272],[-74.78760800000001,40.244323],[-74.78708,40.243807],[-74.786379,40.243123],[-74.78616100000001,40.24291],[-74.785185,40.241972],[-74.78504100000001,40.242114],[-74.784817,40.242342],[-74.784491,40.242664],[-74.784177,40.242983],[-74.783602,40.243544],[-74.783317,40.243832],[-74.78305899999999,40.244083],[-74.782933,40.24418],[-74.782777,40.24403],[-74.7822,40.243551],[-74.781953,40.243353],[-74.781711,40.243182],[-74.781555,40.243084],[-74.78129300000001,40.242922],[-74.780867,40.242663],[-74.780716,40.242583],[-74.780704,40.242576],[-74.78056599999999,40.242512],[-74.780299,40.242401],[-74.780232,40.242374],[-74.779957,40.242248],[-74.77952999999999,40.242064],[-74.779158,40.241901],[-74.779036,40.24184],[-74.77897,40.2418],[-74.778869,40.241753],[-74.777804,40.241292],[-74.777163,40.241013],[-74.77700400000001,40.240943],[-74.77668,40.240803],[-74.776274,40.240635],[-74.775783,40.240454],[-74.775685,40.240393],[-74.775541,40.240303],[-74.77545499999999,40.24025],[-74.774884,40.239925],[-74.774317,40.239603],[-74.773882,40.239349],[-74.77360299999999,40.239194],[-74.77288299999999,40.238791],[-74.77276500000001,40.238724],[-74.77229800000001,40.238455],[-74.77153300000001,40.238026],[-74.771129,40.237795],[-74.77045099999999,40.237397],[-74.770116,40.237214],[-74.77005699999999,40.237182],[-74.769823,40.237058],[-74.76921299999999,40.236703],[-74.768744,40.236396],[-74.768762,40.236371],[-74.768809,40.236302],[-74.76889,40.236196],[-74.768934,40.236142],[-74.769018,40.235999],[-74.769204,40.235727],[-74.76904,40.235631],[-74.768733,40.235427],[-74.76865100000001,40.235373],[-74.768581,40.235327],[-74.76848099999999,40.235259],[-74.768394,40.235196],[-74.76830200000001,40.23513],[-74.767458,40.234551],[-74.76725399999999,40.234411],[-74.766491,40.233887],[-74.766447,40.233856],[-74.76629800000001,40.233762],[-74.76580800000001,40.233465],[-74.76550400000001,40.233284],[-74.76546500000001,40.233261],[-74.764741,40.23284],[-74.76433,40.233201],[-74.764163,40.233364],[-74.76382099999999,40.233697],[-74.763615,40.233906],[-74.76251000000001,40.234989],[-74.761962,40.235527],[-74.76174,40.235743],[-74.76107500000001,40.236393],[-74.760852,40.23661],[-74.760486,40.237014],[-74.76033700000001,40.237164],[-74.759747,40.237739],[-74.758432,40.239019],[-74.75644,40.238267],[-74.754948,40.237705],[-74.754895,40.237756],[-74.75485999999999,40.237792],[-74.75478,40.23787],[-74.754231,40.238406],[-74.753766,40.238861],[-74.753688,40.238936],[-74.753593,40.239028],[-74.753308,40.239307],[-74.753212,40.2394],[-74.752663,40.239946],[-74.75224900000001,40.240355],[-74.752,40.240597],[-74.751963,40.240632],[-74.75181499999999,40.240777],[-74.751454,40.241127],[-74.75107199999999,40.2415],[-74.75068899999999,40.241872],[-74.75060000000001,40.241773],[-74.750129,40.241213],[-74.74983899999999,40.240867],[-74.749593,40.240578],[-74.74934,40.240266],[-74.748999,40.239885],[-74.748942,40.239811],[-74.748845,40.239872],[-74.748189,40.240321],[-74.747823,40.240567],[-74.747669,40.240678],[-74.74745799999999,40.24082],[-74.747035,40.241191],[-74.746788,40.2414],[-74.746691,40.241481],[-74.74611299999999,40.241988],[-74.74583699999999,40.242232],[-74.745664,40.242338],[-74.74526899999999,40.242646],[-74.745031,40.242838],[-74.744951,40.242908],[-74.74471200000001,40.243117],[-74.74403100000001,40.243686],[-74.743923,40.243782],[-74.743791,40.24391],[-74.743745,40.243956],[-74.742749,40.244788],[-74.742704,40.244825],[-74.74244899999999,40.245039],[-74.742288,40.244998],[-74.74223000000001,40.244976],[-74.741152,40.244693],[-74.74069,40.244568],[-74.740168,40.244425],[-74.73965200000001,40.244285],[-74.739569,40.244262],[-74.739052,40.244121],[-74.738091,40.243864],[-74.736957,40.24355],[-74.73644400000001,40.243418],[-74.736254,40.243366],[-74.73618,40.243346],[-74.736109,40.243327],[-74.73594900000001,40.243285],[-74.735911,40.243274],[-74.735776,40.243238],[-74.735659,40.243205],[-74.735579,40.243184],[-74.73549300000001,40.243164],[-74.733969,40.242749],[-74.732991,40.2425],[-74.732299,40.242322],[-74.731791,40.242192],[-74.73178299999999,40.242135],[-74.73178299999999,40.242036],[-74.731796,40.24197],[-74.73181,40.241941],[-74.731829,40.241904],[-74.73189499999999,40.24184],[-74.73209199999999,40.241674],[-74.732421,40.241489],[-74.732888,40.241197],[-74.733311,40.24094],[-74.733453,40.240848],[-74.733656,40.240674],[-74.733822,40.240463],[-74.73410699999999,40.240172],[-74.73438400000001,40.239842],[-74.734661,40.239473],[-74.734695,40.239427],[-74.73475500000001,40.23935],[-74.735004,40.239021],[-74.735045,40.238925],[-74.735084,40.238831],[-74.73522699999999,40.238593],[-74.73550400000001,40.238319],[-74.735677,40.238117],[-74.735784,40.23792],[-74.735882,40.237791],[-74.736047,40.237628],[-74.736619,40.237128],[-74.73704499999999,40.236726],[-74.73711400000001,40.236673],[-74.737301,40.236527],[-74.737436,40.236422],[-74.737635,40.236271],[-74.73779999999999,40.23615],[-74.737853,40.235991],[-74.737863,40.235937],[-74.73786200000001,40.2359],[-74.737861,40.235854],[-74.737871,40.235808],[-74.73788999999999,40.23577],[-74.737932,40.235712],[-74.73801,40.235598],[-74.73805,40.235531],[-74.73808699999999,40.23544],[-74.738105,40.235368],[-74.738122,40.235288],[-74.73813699999999,40.235219],[-74.738168,40.235121],[-74.73818,40.235083],[-74.738204,40.235037],[-74.738237,40.234984],[-74.738277,40.234941],[-74.73834100000001,40.234885],[-74.73840800000001,40.234814],[-74.738457,40.234729],[-74.738477,40.234687],[-74.73849800000001,40.234668],[-74.73851999999999,40.234657],[-74.738563,40.234644],[-74.738558,40.234489],[-74.73854900000001,40.234377],[-74.738528,40.234281],[-74.738508,40.234184],[-74.738478,40.234106],[-74.738434,40.234032],[-74.73819899999999,40.233712],[-74.73813800000001,40.233606],[-74.738107,40.233537],[-74.738013,40.233234],[-74.737936,40.23298],[-74.73791,40.232889],[-74.737886,40.232803],[-74.737863,40.232693],[-74.737849,40.232568],[-74.737858,40.232471],[-74.737898,40.232392],[-74.737965,40.232319],[-74.738068,40.232231],[-74.73832400000001,40.232067],[-74.73885,40.231729],[-74.73918999999999,40.231578],[-74.739289,40.231545],[-74.73936999999999,40.231522],[-74.73938800000001,40.231516],[-74.73947800000001,40.231507],[-74.739423,40.231452],[-74.739328,40.231356],[-74.738828,40.230853],[-74.73864,40.230665],[-74.738462,40.230487],[-74.73802000000001,40.230048],[-74.737731,40.229754],[-74.736988,40.229009],[-74.736638,40.228664],[-74.73619600000001,40.228216],[-74.735235,40.227252],[-74.73439399999999,40.22641],[-74.734239,40.226255],[-74.734126,40.226142],[-74.733695,40.225709],[-74.732854,40.224867],[-74.73208,40.224092],[-74.73140100000001,40.223412],[-74.730987,40.222998],[-74.730515,40.222524],[-74.730456,40.222449],[-74.730239,40.222233],[-74.72993700000001,40.221947],[-74.729789,40.221753],[-74.729411,40.221373],[-74.728808,40.220768],[-74.728904,40.220743],[-74.729264,40.22065],[-74.72961599999999,40.220559],[-74.73011,40.220428],[-74.730527,40.220315],[-74.730626,40.22029],[-74.730692,40.220272],[-74.730953,40.220198],[-74.73280699999999,40.21971],[-74.732721,40.219622],[-74.732373,40.21927],[-74.732302,40.219202],[-74.731741,40.218633],[-74.731572,40.218472],[-74.73116,40.218064],[-74.730818,40.217725],[-74.730593,40.217496],[-74.73015100000001,40.217055],[-74.73001600000001,40.216914],[-74.729966,40.216865],[-74.729816,40.216715],[-74.729765,40.216665],[-74.72998,40.216491],[-74.731166,40.215408],[-74.73138299999999,40.215211],[-74.731431,40.215169],[-74.7315,40.215105],[-74.731775,40.214854],[-74.732409,40.214276],[-74.732983,40.213754],[-74.733379,40.213393],[-74.733632,40.213163],[-74.73427,40.212581],[-74.734545,40.212333],[-74.734616,40.212267],[-74.7347,40.212187],[-74.73488,40.212023],[-74.734892,40.212011],[-74.734988,40.211925],[-74.735367,40.211582],[-74.735387,40.211563],[-74.735581,40.211388],[-74.735738,40.211244],[-74.73598200000001,40.211021],[-74.736149,40.210877],[-74.736197,40.210831],[-74.736783,40.210292],[-74.737041,40.210058],[-74.737106,40.21],[-74.73742300000001,40.209708],[-74.73727700000001,40.209513],[-74.737081,40.209251],[-74.73681999999999,40.208911],[-74.73657900000001,40.208599],[-74.736351,40.2083],[-74.736293,40.208225],[-74.736069,40.207933],[-74.735513,40.20721],[-74.735373,40.207029],[-74.734948,40.206475],[-74.734869,40.206373],[-74.734633,40.206065],[-74.73455300000001,40.205962],[-74.734442,40.205818],[-74.733892,40.205104],[-74.733513,40.20461],[-74.733417,40.204486],[-74.732918,40.203839],[-74.732715,40.203573],[-74.73256499999999,40.203391],[-74.73289,40.203023],[-74.733205,40.202668],[-74.733265,40.202599],[-74.73327999999999,40.202583],[-74.733486,40.202351],[-74.73371,40.202097],[-74.733763,40.202039],[-74.733811,40.201983],[-74.734036,40.201732],[-74.734313,40.201415],[-74.734386,40.201332],[-74.73461399999999,40.201075],[-74.734979,40.200663],[-74.735277,40.200786],[-74.735432,40.200791],[-74.735519,40.200785],[-74.735857,40.200732],[-74.736644,40.200614],[-74.73698,40.200567],[-74.73730999999999,40.200521],[-74.737448,40.200501],[-74.73799699999999,40.200424],[-74.738168,40.2004],[-74.73819899999999,40.200395],[-74.738249,40.200388],[-74.7384,40.200369],[-74.73845,40.200362],[-74.73909,40.20027],[-74.739971,40.200145],[-74.740106,40.200126],[-74.74085599999999,40.20002],[-74.740999,40.199999],[-74.741241,40.199965],[-74.741342,40.19995],[-74.74174499999999,40.199893],[-74.741901,40.199871],[-74.742626,40.199768],[-74.743013,40.199714],[-74.743527,40.199641],[-74.743757,40.199608],[-74.744027,40.199571],[-74.74440199999999,40.199518],[-74.746011,40.199291],[-74.746128,40.199275],[-74.746182,40.199267],[-74.74659800000001,40.199208],[-74.746768,40.199185],[-74.74744699999999,40.19909],[-74.74753200000001,40.199077],[-74.74786899999999,40.199028],[-74.748192,40.198984],[-74.748327,40.198963],[-74.749185,40.198843],[-74.749211,40.19884],[-74.749702,40.198771],[-74.75010899999999,40.198722],[-74.750305,40.198701],[-74.75098,40.198606],[-74.751065,40.198592],[-74.752681,40.198364],[-74.75276599999999,40.198351],[-74.752841,40.19834],[-74.75269400000001,40.197652],[-74.75257000000001,40.197192],[-74.75247299999999,40.19678],[-74.75238,40.19635],[-74.75228300000001,40.195975],[-74.751784,40.194011],[-74.751762,40.193951],[-74.75172499999999,40.193838],[-74.751614,40.193395],[-74.751588,40.193287],[-74.75133700000001,40.19228],[-74.751302,40.192192],[-74.75127999999999,40.192163],[-74.75123000000001,40.192099],[-74.75120200000001,40.191997],[-74.750979,40.191193],[-74.75063299999999,40.190248],[-74.750407,40.189628],[-74.75036799999999,40.189558],[-74.750097,40.189052],[-74.749961,40.18889],[-74.749855,40.188757],[-74.748699,40.18735],[-74.748521,40.187215],[-74.748195,40.186971],[-74.748182,40.186961],[-74.748169,40.186951],[-74.747709,40.186607],[-74.74688399999999,40.186105],[-74.746498,40.185871],[-74.746104,40.185684],[-74.746593,40.185521],[-74.746948,40.18541],[-74.747185,40.185334],[-74.749163,40.184693],[-74.750237,40.184347],[-74.751176,40.18404],[-74.751684,40.183875],[-74.75176,40.183839],[-74.752286,40.184122],[-74.75245099999999,40.184211],[-74.752646,40.184316],[-74.75271100000001,40.184351],[-74.752734,40.184363],[-74.752747,40.18437],[-74.75286800000001,40.184435],[-74.754305,40.185209],[-74.75557499999999,40.186674],[-74.755605,40.186709],[-74.75662800000001,40.188833],[-74.756759,40.189105],[-74.756905,40.189409],[-74.757239,40.190372],[-74.757615,40.191458],[-74.75815299999999,40.193009],[-74.758213,40.193182],[-74.758223,40.19321],[-74.758476,40.193941],[-74.758487,40.193972],[-74.759209,40.196054],[-74.759505,40.196909],[-74.759603,40.197088],[-74.759714,40.197289],[-74.760169,40.198116],[-74.76020200000001,40.198176],[-74.760605,40.198909],[-74.76061799999999,40.198927],[-74.760837,40.199213],[-74.760851,40.199232]]) # create polygon
point = Point(-74.74294,40.21705) # create point
print(polygon.contains(point)) # check if polygon contains point
print(point.within(polygon)) # check if a point is in the polygon



import dropbox

import addfips
af = addfips.AddFIPS()
print(af.get_county_fips('Cook County', state='Illinois'))
