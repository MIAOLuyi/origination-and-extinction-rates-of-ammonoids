#!/usr/bin/env python
from numpy import * 


data_1=[array([188.90085]),
array([188.811127,189.333531,188.901701,189.129894,189.108053,188.846404,189.188877]),
array([188.888405,189.464959,188.882736,188.935039,189.152439,189.450941,189.35991,189.24843,189.384159,189.370683,189.256918,189.141232,189.345564,189.088104,189.409097,189.18562,189.054225,189.470932,189.109621,189.021636,189.084766,188.82803,188.944476]),
array([188.970165,189.321003,189.081896,188.902676,189.241952,189.430296,188.882588,188.951837,189.155816,189.490861,188.91085]),
array([189.437941,188.965366,189.119192,189.084695,189.218673,189.362061,189.024771,189.410384,188.905197,189.119012]),
array([188.953019,189.3384,188.887228,189.105088,189.352519,188.883424,188.925168,189.395586,188.935542,189.02615,188.897748,189.460952,189.097345,188.881425,189.409231,189.204691,189.35764,189.050746,189.444039,189.022943,189.406367,189.406172]),
array([189.684513]),
array([189.042918,189.414852,188.838254,189.336257,188.97246,188.933179,188.987865,189.47845,189.005628,188.988594,189.055159,189.26318,188.974555,188.849997,188.870749,189.395046,188.992455,189.244348,188.899079,188.843268,189.405827,189.319513,189.414648,188.846857,189.275871,189.143379]),
array([188.227066,188.223555,188.213258,188.229875,188.230782,188.23334,188.226603,188.212886,188.229958,188.215825,188.231291,188.225534]),
array([188.21395,188.216078,188.232055,188.223723,188.23361,188.229021,188.218212,188.22547,188.217607,188.223596,188.229226,188.23317,188.22006,188.222856,188.221535,188.234105,188.228653,188.223526,188.233211,188.23521,188.212856,188.23819,188.237773,188.210875,188.226015,188.214317,188.237936,188.227581,188.238809,188.22619,188.2374,188.239382,188.22471,188.223231,188.236192,188.230352,188.21757,188.216373]),
array([188.234911,188.233846,188.22818,188.226455,188.214019,188.211242,188.234872,188.23578,188.228448,188.234761,188.225257,188.219758,188.215659,188.225149,188.227491,188.23931]),
array([188.398957,188.353302,188.370273,188.309819,188.282453,188.275163,188.390578,188.277456,188.286323,188.311975,188.334958,188.357422,188.341563,188.379867,188.383189,188.304402,188.257084,188.305318,188.329971,188.354137,188.373209,188.308753,188.311613,188.353363,188.26921,188.319868,188.272849,188.390365,188.318998,188.311308,188.368185,188.32309,188.376257,188.376514]),
array([188.335963,188.335509,188.360849,188.296281,188.290145,188.367856,188.296769,188.396997,188.285562,188.369656,188.287546,188.377345,188.358587,188.272016,188.283226,188.293591,188.311464,188.277484,188.325874]),
array([192.306727,192.76231,191.312602]),
array([192.543631,191.961521,192.291224,192.786397,192.027834,191.860093,192.451061,192.253131,191.848361,192.626428,192.53798,192.050823,191.852053,192.754357,192.33418,192.328971]),
array([189.216302,188.698234,188.33053,189.388978,189.146706,189.447859,189.287741,188.855689,189.252123,189.088783,187.7436,186.59353,187.352612,187.768894,183.920187]),
array([190.22667,189.002325,190.039913]),
array([189.192184,188.837936,188.86021,189.442554,188.969779,189.277126,189.07729,188.991355,188.839738,188.923022,189.040128,189.400793]),
array([188.612027,188.697325,188.437007,188.48977,188.54836,188.69945,188.790875,188.749937,188.417378,188.474864,188.734164,188.519929,188.436325,188.799003,188.479225,188.467587,188.589703,188.748891,188.793354,188.756342,188.540955,188.731396,188.683676,188.475041,188.531411,188.798169,188.686506,188.621001,188.505656,188.43653,188.701279,188.766195,188.753413,188.426351,188.419111,188.572343,188.539175,188.575742]),
array([188.5596,188.554431,188.714128,188.593991,188.654037,188.42687,188.725683,188.631202,188.637582,188.603989,188.720795,188.78419,188.573474]),
array([188.63364,188.520337,188.561319,188.641389,188.55651,188.758979,188.787627,188.524376,188.474316,188.736885,188.660379,188.629147,188.492194,188.45349]),
array([189.301446,188.230192,188.083555,188.119862,188.166507,188.821478,188.118916,188.092677,188.874551,188.236281,188.229211,188.180551,188.039071,188.236415,188.080871,188.166015,188.18753,188.055668,188.021392,188.061296,188.213256,188.229044,188.192469,188.236826,188.216752,188.135934,188.01615,188.114463,188.116706,189.481212,188.094997,189.095848,188.052023,188.220813,188.148879,188.223757,188.175633,189.396598,189.080445,188.485608,188.019095,188.237089,185.597985,187.742551,187.145596,185.845189,187.884445]),
array([188.584163]),
array([188.313963,188.363032,188.579091,188.023604,188.231685,188.090515,188.203142]),
array([192.632311]),
array([188.792978,188.111629,189.543991,188.272723,188.28218,189.33132,189.270836,188.448074,191.902453,192.371621,189.234618,189.98635,192.065559,191.615522,190.047787,193.24385,187.486575,187.057749,185.898012,183.760266]),
array([191.981852,192.001114]),
array([188.423961,189.259819,188.59964,188.639478,190.160861,190.397156,188.274754,188.112513,188.39642,191.999212,188.86709,191.078275,188.682021,190.032072,191.882127,190.758869,189.812734,188.927557,191.149385,186.603741,187.016178,186.655818,187.158408,185.503057,183.231906,184.784964]),
array([191.806377,191.637585]),
array([192.854667,191.92573,192.128918,192.821517]),
array([192.390454,192.503084]),
array([192.480771,192.231567]),
array([192.225902,191.86844]),
array([190.210931,190.468276,190.503821,190.406214]),
array([190.478384,191.473451,190.82666,190.54603,191.044498,191.815219]),
array([191.383963,192.869454,191.320901,191.027861,191.073032,191.802854]),
array([191.803546,192.315014,192.172325,191.135896]),
array([191.790762,191.214528,191.099093,191.749151,190.864113,191.088294,191.784027]),
array([191.130383]),
array([188.838036]),
array([188.449001,189.744838,189.011325,188.216809,188.573085,188.641553,188.207554,188.988735,188.178531,188.201349,188.088451,189.7322,188.148897,190.181109,189.48515]),
array([188.901628]),
array([189.756329,189.064382,189.000443,189.27939,189.65584,189.47731,188.88975,189.474446]),
array([189.188071]),
array([189.017159,189.2384,189.384249,189.496469]),
array([189.413624,189.044115]),
array([188.952729]),
array([188.800505,189.321296]),
array([192.863474]),
array([189.41863,188.920359,188.961606,189.176661,189.059097,189.120443,188.540372,188.967418,189.085507,189.375188,189.422003]),
array([188.943908,188.902536,189.086872,190.269979,188.974032]),
array([190.848105]),
array([191.953087,191.863158]),
array([191.443994,192.34458,191.428722,191.669362,191.097486]),
array([192.221833]),
array([191.344429,191.069859]),
array([189.465801]),
array([188.948497]),
array([192.765871,191.888946,192.395384]),
array([192.085679,192.171688]),
array([188.126655]),
array([188.356165]),
array([188.196593,188.35001,188.091308]),
array([188.397314,188.112221,188.1941,188.099449,188.255199,188.1855,188.094827,188.303521,188.179155,188.347921,188.153893,188.068297,188.270511,188.24111]),
array([189.106887,189.404022,188.937082,188.898651,189.165793,188.693229,189.038019,189.323766,189.49961,189.123399,189.425135]),
array([188.398727,188.140276]),
array([189.046304]),
array([188.53009]),
array([189.305141,188.82839,188.985466]),
array([190.439861,191.491878]),
array([188.665434]),
array([188.878971,188.563226,189.238709,188.753685,189.197628,188.973901,189.68514,189.00005,189.267763,189.394184,188.735493,189.53639]),
array([189.984323]),
array([188.339433]),
array([189.557892]),
array([188.229675,188.173276,188.222316,188.01056,188.22169,188.220674]),
array([188.706153,188.512444,188.426351,188.520187,188.334888,188.320818,188.530101,188.659109,188.627371,188.299955,188.49578,188.397694]),
array([192.652736]),
array([191.961129,192.597321]),
array([192.096839,189.724663,189.076842,189.604537,192.672172,191.65995,190.887636,189.475628,192.584854,188.673792,188.337015,189.391361,192.201302,191.502898,188.442677,193.676222]),
array([190.87875,190.831294,190.725045,191.666282,190.496764,191.492224]),
array([192.587479,192.597832]),
array([190.929537]),
array([190.068561]),
array([188.02998,188.183844]),
array([191.394069,191.129841,190.715839,190.684702,189.153491,192.456353,190.224124,188.496933,190.63913]),
array([191.605443]),
array([190.441809,190.703678,191.303883,191.035252]),
array([189.378462]),
array([188.662908,188.926803,189.45398,188.305189,188.072355,188.125515,189.289683,189.083028,189.453358,189.095851,188.636456,189.234555,188.727921,187.483013,185.872645,187.763697,187.291629]),
array([188.927188,189.944445,188.986607]),
array([191.290832,192.609807,191.848119,190.553039]),
array([192.366788,191.809139,192.024462,192.367597,192.71218]),
array([190.838965,190.721835,190.605306]),
array([192.401751]),
array([188.913862,192.208177,188.606491,189.554872,189.014662,188.599252,188.891527,189.187643,188.140546,190.09383,189.357752,192.57478,190.612897,189.392099,192.344438,190.326702,190.11118,190.941558,188.514379,190.206882,191.62493,190.199505,189.838023,191.771245,191.01894,189.925197,189.538611,192.865665,194.371942,193.231555,193.481654,183.57658,187.533913,187.152346,184.330278]),
array([193.819521,192.642863,190.605918,190.723858,192.389924,190.904865,191.920138,194.033911,194.274029,193.395853]),
array([188.899305]),
array([192.317638,194.364632]),
array([188.604849,189.239243,188.850653,189.09938,188.449676,189.104207,188.939244,188.868174,189.029365,188.753483,188.407143,188.739694,189.125692,189.257243,188.947183,189.182399,189.308231,189.368579,189.299304,189.629804,189.450083]),
array([188.412303,188.552335,188.696368,188.215216,188.341247,188.419998,188.759791,188.19558,188.721134,188.384803,188.72296,188.224385,188.423762,188.430235,188.249259,188.449217,188.377499,188.784069,188.288945,188.637438,188.796182,188.338497,188.523066,188.518551,188.571486,188.259022,188.046022,188.754333,188.639167,188.308607,188.669591,188.691037,188.554401,188.329099,188.433758,188.157903,188.552606,188.152995,188.187216,188.624289,188.57701,188.559674,188.5504,188.060255,188.630305,188.269428,188.147441,188.256234]),
array([188.097204,188.066433,188.094977]),
array([188.487315]),
array([190.65347,190.251161,190.680259,190.381761,190.697421,192.30639,192.07166,196.076558,196.925684]),
array([188.689771,190.495946,190.316643,190.318401,189.620027,188.360185,188.564938,188.244417,190.392448,192.853877,190.232327,192.709326,191.428942,191.641044,189.048119,188.203757,188.082008,188.389502,188.222652,188.212564,188.259426,189.227475,188.54164,188.248088,188.2299,188.158927,189.324189,188.731238,188.347787,188.219469,188.098723,188.180414,188.538813,189.558382,188.226704,188.167742,189.45625,188.586545,188.362405,188.236552,188.170233,188.660379,189.172909,189.129572,188.452998,188.286479,188.215075,188.009546,190.256194,189.415828,188.125756,189.458036,188.632098,188.374937,188.211172,188.034136,188.766124,188.134219,190.597492,189.912852,188.600581,188.112278,191.204743,190.176322,190.297237,190.971305,191.165094,190.472978,190.715996,188.281047,188.617037,190.382686,190.74262,191.749711,189.954021,192.047779,188.380525,188.747467,189.321125,190.002654,189.439643,188.535254,188.316112,186.919445,187.955089,186.203908,186.075803,185.688678,187.097197,186.539213,185.880389,187.809803,186.60849,186.027086,186.123348,186.972739,187.69594,187.61699,186.208411,185.658102,186.440889,187.85107,187.008433,187.016462,186.857303,185.762386,184.390059,185.168293]),
array([191.64681,188.712085,193.218109]),
array([191.909083]),
array([191.62816]),
array([190.341647]),
array([188.174783,189.859657,188.339528,188.310395,189.580721,188.550693,189.608687,188.358661,188.65548,188.567594,188.521446,189.697328,191.598238,185.59731,187.828253,186.904376,187.171296,186.595934,187.20451,186.552753]),
array([192.314106]),
array([192.378148,191.989569,192.707756]),
array([189.219824]),
array([191.839653,190.565474]),
array([189.23639,189.451784,189.244648,189.392736,189.30505,188.900244,189.342555,189.404867,189.129666,189.440161,189.146222,189.308678,188.909458,189.14448,188.897125,188.900133,189.302394,189.348453,188.999166,189.366923,189.030683,188.943867,189.075873]),
array([190.549462,190.58861,190.579214,190.705527,190.734112,190.701753,190.580703,190.54912,190.632738,190.695948,190.631398,192.093229,190.729681,190.625662]),
array([190.681082,190.722345]),
array([190.353751]),
array([189.290974,189.052754,189.103294,188.86778,188.899467,189.443554,189.100273,188.835315,189.392418,189.252203,189.198537,188.994271]),
array([191.649053]),
array([191.107822]),
array([191.4003,192.689622,191.341004,191.116853,191.158493,191.135838,191.207936,190.895314,191.080925]),
array([191.835896,190.872703,190.545008,191.026934,191.277318,190.712041,191.714467,191.213736,191.011451,191.7974,191.317736]),
array([191.063408,192.724099,192.289607]),
array([188.113166,188.139742,188.011612,188.209542,188.179582,188.053726,188.153252,188.1582,188.138923,188.026832,188.046565,188.191157,188.022796]),
array([188.168742,188.203114,188.088118,188.034853,188.083501,188.096534,188.195845,188.096325,188.045202,188.049411,188.203906,188.100306,188.073759,188.08771,188.187402,188.197502,188.113564,188.13893,188.206421,188.034901,188.147921,188.039361,188.201095,188.104922,188.115481,188.063655]),
array([192.173371]),
array([191.940427,192.387208,192.662603,192.361766,192.21591,192.86348,194.124532]),
array([191.01878]),
array([191.008056,190.906525,190.920969,191.604959,191.328263,190.902214]),
array([190.653474,190.698032,190.760703,190.622719]),
array([192.81377]),
array([191.191102,191.329028]),
array([192.663628,190.578344,191.255168,192.454107,190.596512,190.215817,191.34272,191.52481,192.048471,191.091485,190.598489,190.542464,190.282269]),
array([189.63687,189.656589,189.334344,191.719645,191.384721,191.15765,188.054693,189.100881,189.321183,192.659073,192.097431,190.162066,190.01575,188.787712,190.794438,190.047108,189.048552,189.201673,195.918965,194.093367,195.631296,193.924651,193.829017,186.668377,187.522678,185.373576]),
array([192.304117]),
array([190.726866]),
array([188.024362,188.680864,188.364886,188.009713,188.252504,185.990591]),
array([192.130616,192.077097,192.792139,191.985991,192.416868,191.85256,191.862337,192.691881,192.779117,192.569358,190.252807,192.311758,192.89051,192.143077,192.607535,192.071131,192.215311,193.541832,193.207089]),
array([190.750869,192.381421,188.662519,190.166396,192.857036,191.225266,192.341164,192.388101,191.115168,190.284987,189.324288,192.837685,193.486099,194.203642]),
array([191.701861,192.870732,190.533415,191.467722,192.736993,188.280349,188.153707,192.045209,188.752991,188.074285,190.101746,188.373841,190.798833,192.193144,188.090572,192.592716,190.226355,192.819889,189.473915,188.906783,188.604364,188.717033,188.239314,191.902328,192.288421,192.802213,191.458914,189.582427,188.600037,194.296688,193.647916,186.489112,186.526141,187.001507]),
array([190.730577]),
array([190.631931]),
array([190.61124,190.550897,190.676886,190.561566,190.554015,190.770991,190.732566,190.655493,190.615002,190.643041,190.668198,190.735077,190.575196,190.733922,190.709945,190.701932,190.566608,190.71933,190.723369]),
array([190.625785,190.759942,190.666095,190.740293,190.620435,190.7565,190.718922,190.626656]),
array([190.768204,190.60907,190.774986,190.621102,190.648293,190.69352,190.672724,190.669714,190.595905,190.755269,190.592801,190.660869,190.767067,190.747844,190.646021,190.548125,190.636038,190.560126,190.559272,190.742011,190.684711,190.640437,190.602636,190.607917,190.773583,190.765107,190.620556,190.595918,190.638152,190.725843,190.695642,190.661518]),
array([191.90419,191.626085,191.173855,191.577757,191.150271,190.91017,190.97645]),
array([190.767675]),
array([190.692463,190.689894,190.741524,190.607534,190.60749]),
array([189.116123]),
array([190.720506]),
array([190.265986,190.372569,190.217421,190.280992,190.439133,190.494513,190.502397,190.30287,190.370337,190.405918,190.350845,190.517905,190.425365,190.334768,190.495124,190.329787,190.335388,190.457912,190.31215]),
array([190.753092,190.786914,190.927351]),
array([190.153248]),
array([191.415878,190.610952,191.314657,190.605231,190.315897,190.961706,190.853696,191.333317,191.54645,190.592241,191.459628,191.298184,190.885619,190.891754,191.787097,190.371544]),
array([191.861237,192.741638]),
array([188.210064,188.223632,188.213874,188.216128]),
array([188.227361,188.162049,188.225392,188.019833,188.235182,188.177784,188.212922,188.083676,188.239422,188.201883,188.215283,188.136054,188.223119,188.101148,188.22083,188.078385,188.227609,188.025572,188.224108,188.049388,188.235423,188.167941,188.215856,188.198843,188.214956,188.12942,188.234906,188.090268,188.227902,188.082678,188.214004,188.179689,188.223745,188.000497,188.223685,188.081953,188.22582,188.033442,188.220316,188.065515,188.233242,188.170836,188.232192,188.018366,188.234121,188.104257,188.22037,188.129929,188.222547,188.198468,188.221826,188.179452,188.211285,188.049919,188.235788,188.113186,188.217274,188.200602,188.214239,188.198954,188.224225,188.054605]),
array([188.238111,188.22953]),
array([192.708785,192.851334]),
array([192.206794]),
array([190.380626,190.712306,191.650707]),
array([190.940626,192.174302,190.879121,192.807351,192.869844,190.502152,190.657282,190.649691,192.064142,194.150641]),
array([192.183705,191.809985,190.66864,191.689631,192.040876,190.634933,191.595472,191.363903,192.015957,190.635825,191.097273,190.416923,190.583542,190.533708,191.953738,190.58585,192.069518,192.136687,191.709815,192.128815,191.786172,192.067043,191.246498,191.88057,192.525852,192.020824]),
array([188.091494]),
array([190.121609,188.511518,191.463716,191.164047,190.866782,191.791395,192.444354,191.28112,189.400192,188.60912,190.413838,190.352739,190.270932,191.65277,190.758814,188.318394,189.393872,190.412763,188.776877,192.26873,192.118251,190.478503,189.44444,188.614528,191.106368,190.837332,189.560851]),
array([188.584956,188.24508]),
array([189.24373,188.727243,188.615701,189.252998,189.483399,188.791058,188.485534,188.561236]),
array([188.649326,188.794922,188.253329,188.339177,188.305765,188.479885]),
array([188.615339,189.365564,188.447599,188.571276,188.662286,188.70856,189.218759]),
array([189.401975,188.66886,188.923735,188.665179]),
array([188.357846,188.346757]),
array([192.386543]),
array([188.863812]),
array([192.785533,190.416328]),
array([192.29184]),
array([192.492828,192.322526,192.145013,193.487467]),
array([192.155995,192.784794,192.395462,192.846766,192.229544,192.501059]),
array([188.709068,189.195022,188.975246,188.430787,189.492135,188.828957]),
array([188.938348,188.907089,189.255496,188.831729,189.444473,189.135235,188.984858,189.368852,189.18278,188.836876,189.342811,189.347024,188.888331,189.160132,188.98081,189.372181]),
array([188.834147,188.336685,188.904592,189.331659,188.004975,188.653024,188.821018,189.432255,188.504386,188.087129,188.225934,190.120044,188.38886,188.451577,188.562701,188.600088,188.362127,188.793109,188.541007,188.233595,188.00812,189.440326,188.218699,189.866757,188.953377,186.543539]),
array([192.178466,191.721886,190.460192,192.312126,191.195123,190.620065,190.912231,191.228587,191.308246,190.444116,189.770347,190.950324,191.291232,191.052391,189.612629,189.714172,190.327624,192.435105]),
array([190.489257,190.648182,189.074639,190.443226,189.056142,189.128225,189.652496,188.870377,189.058938,189.236674,188.990012,189.397531,189.694209,189.195399,189.076857,188.419617,189.105124,189.104457]),
array([190.068315,190.053133,190.161599,189.928902,189.585424,189.902946,190.218565,189.942503,190.256556,190.427854,190.081786]),
array([188.99801,190.491693,188.873447,189.934199,190.479962,189.716156,190.246323,189.975092,190.14492,189.960393,190.383492,189.510875]),
array([190.303989,189.901412,190.214059,189.04472,190.323564]),
array([189.905836,190.772219,189.663725,190.595988,190.019798,189.529984,190.708135,190.459503]),
array([189.415057,189.70656,189.527415,190.417196,189.281772,190.273088,189.795377,189.464932,190.245796,189.547067,190.371837,190.317079,190.063423,190.220278,190.350308,189.585066,190.488152,189.803441]),
array([189.721372,189.851814,189.580714,190.089263,190.042441,189.886116,190.077007,190.074673,189.708149,189.798809,189.938174,190.015507,189.998399,189.761155,189.998939,189.991926,190.099852,189.583994,190.020221,190.103986,189.87211,189.714779,189.723193,190.056414,189.957454,189.700397,190.164713,189.798533,189.521458,190.16044,189.749226,189.515603,189.802125,190.044764,189.775552,189.551333,189.707433,189.711748]),
array([190.335446,189.852776,190.435601,190.487559,190.12103,190.029749,190.085552,189.940099,189.824938,189.904951,190.444731,189.764831,189.803433,190.098242]),
array([190.512394,189.509669,190.364961,190.21347,190.340636]),
array([188.643906]),
array([190.444426,190.122716,190.024941]),
array([189.255986,189.125334,189.440852,189.6528,189.895996,189.987482,188.849498]),
array([188.738619]),
array([188.657676,189.833029]),
array([189.235153,188.991826,189.142068,189.05863,189.000668,189.317221,189.051959,188.846843,189.419944,189.381107,189.067221,188.938131,188.940175]),
array([188.988259]),
array([189.359342]),
array([190.234511]),
array([190.502974,190.3603,190.43509,190.426536,190.442664,190.388804,190.398393,190.337084,190.439397,190.243045,190.20129]),
array([190.479294,190.238333,190.377971,190.305649,190.35056,190.415412,190.322233,190.306977,190.529597,190.250886,190.472957,190.37544,190.352512,190.324458]),
array([190.409118,190.27671,190.486056,190.268098,190.371575,190.217205,190.284748,190.26955,190.430405,190.459983,190.246277,190.348717,190.328103,190.511672,190.363445,190.268323,190.365155,190.438055,190.512091,190.285168,190.513442,190.370478,190.380825,190.507722,190.516885,190.52976,190.324936,190.448786,190.477181,190.256993,190.468474,190.402841,190.461929,190.520047,190.293378,190.536505,190.371648,190.383923,190.365542,190.379952,190.47943,190.350813,190.482881,190.346911,190.216877,190.289964,190.23227,190.336709,190.454393]),
array([192.357054,192.024921,192.650179]),
array([192.688135,192.877264,192.069984,192.401409]),
array([191.84312]),
array([191.051953,192.032623,192.083309]),
array([189.068851]),
array([189.611406]),
array([190.395173]),
array([192.393862,193.393233]),
array([192.276736,188.843538,191.654148,191.614434,190.467038,189.763748,190.852664,188.228207,188.03528,190.166142,189.306488,188.47207,189.556878,192.732908,191.444282,191.592418,190.913422,190.287607,192.360754,192.587385,191.778884,193.689189,193.433526,195.751955,193.247765,192.946741,185.715609,185.620207,184.794285,185.466821,184.185641])
]

d=[data_1]
names=[ 'eP_oc_1']
def get_data(i): return d[i]
def get_out_name(i): return  names[i]
taxa_names=['Acanthopleuroceras?_sp._nov._2','Acanthopleuroceras_actaeon','Acanthopleuroceras_alisiense','Acanthopleuroceras_arietiforme','Acanthopleuroceras_carinatum','Acanthopleuroceras_maugenesti','Acanthopleuroceras_sp.1','Acanthopleuroceras_valdani','Aegoceras_artygyrus','Aegoceras_capricornus','Aegoceras_lataecosta','Aegoceras_maculatum','Aegoceras_sparsicosta','Aegolytoceras_varicosum','Apoderoceras_aculeatum','Audaxlytoceras_audax','Baltzerites_baltzeri','Beaniceras_centaurus','Beaniceras_crassum','Beaniceras_luridum','Beaniceras_rotondum','Becheiceras_bechei','Bettoniceras?_perisphinctoides','Bettoniceras_italicum','Bifericeras_donovani','Calaiceras_calais','Caleites_calensis','Calliphylloceras_bicicolae','Capreoliceras_asagensis','Castanayiceras_canavarii','Catriceras_catriense','Catriceras_cf._campiliense','Catriceras_galaczi','Coeloceras_pettos','Coeloceras_pettos_sensu_G','Coeloderoceras_biruga','Coeloderoceras_micromphala','Coeloderoceras_ponticum','Coeloderoceras_rugosa','Cymbites?_laevigatus_sensu_RG','Cymbites_globosus','Dayiceras_amaltheiforme','Dayiceras_dayiceroides','Dayiceras_nanum','Dayiceras_polymorphoides','Dayiceras_renzi','Dayiceras_splendens','Diaphorites_vetulonius','Dubariceras??_sp.','Dubariceras_dubari','Dubariceras_inaequicosta','Eoderoceras?_lina','Epideroceras?_cantianense','Epideroceras?_nodofissum','Epideroceras?_plumarius','Epideroceras?_trigonale','Eremiticeras_evolutus','Fieldingiceras_sp.','Foetterliceras_morogense','Foetterliceras_salmojraghii','Fuciniceras_angulosum','Fuciniceras_balatonense','Fuciniceras_carixiense','Fuciniceras_costicillatum','Fuciniceras_dilectum','Fuciniceras_elichense','Fuciniceras_formosum_sensu_RG','Fuciniceras_giennense','Fuciniceras_hungaricum','Fuciniceras_ionicum','Fuciniceras_lycius','Fuciniceras_mellahense','Fuciniceras_n._sp._A','Fuciniceras_nov._sp.1','Fuciniceras_perplicatum_sensu_GM','Fuciniceras_pseudodilectum','Fuciniceras_volubile','Furlites_involutus','Galaticeras?_rosenbergi','Galaticeras_aegoceroides','Galaticeras_harpoceroides','Galaticeras_marianii','Gemmellaroceras?_cortesi_sensu_B','Gemmellaroceras?_gemmellaroi','Gemmellaroceras?_gemmellaroi_sensu_M','Gemmellaroceras_aenigmaticum','Gemmellaroceras_circumcrispatum','Gemmellaroceras_granuliferum','Gorgheiceras_gorghense','Harpophylloceras_eximus','Holcolytoceras_nodostricum','Holcolytoceras_quadrijugum','Hyperderoceras_retusum','Jamesonites?_spoliatus','Jamesonites_reticulatus','Juraphyllites_libertus','Juraphyllites_nardii','Juraphyllites_sp._A','Leptonotoceras_sp.','Liparoceras_cheltiense','Liparoceras_heptangulare','Liparoceras_lytoceroides','Lytoceras_altum','Lytoceras_fimbriatoides','Lytoceras_fimbriatum','Lytoceras_fuggeri','Lytoceras_galatiforme','Lytoceras_kizilcius','Lytoceras_platypleura','Lytoceras_tortum','Metaderoceras?_pygmaeus','Metaderoceras_apertum','Metaderoceras_beirense','Metaderoceras_clavatus','Metaderoceras_gemmellaroi','Metaderoceras_muticum','Metaderoceras_muticum_sensu_MB','Metaderoceras_pseudomuticum','Metaderoceras_venarense','Miltoceras?_sp.','Miltoceras_furlense','Miltoceras_seguenzae','Miltoceras_sellae','Miltoceras_taguendoufi','Oistoceras_angulatus','Oistoceras_figulinum','Paraderoceras_picenum','Paramicroderoceras_aff._birchiades','Paramicroderoceras_birchoides','Paramicroderoceras_fila','Paramicroderoceras_tardecrescens','Paramorphites_acutiventris','Paratropidoceras_numidianum','Parinodiceras_parinodus','Partschiceras_striatocostatum','Pelingoceras_pseudocarinatum','Peripleuroceras_rotundicosta','Phricodoceras_bettonii','Phricodoceras_taylori','Phricodoceras_taylori_sensu_H','Phylloceras_hebertinum','Platypleuroceras_acanthobronni','Platypleuroceras_aff._oblongum','Platypleuroceras_amplinatrix','Platypleuroceras_aureum','Platypleuroceras_brevispina','platypleuroceras_caprarium','Platypleuroceras_muellensis','Platypleuroceras_nodosum','Polymorphites?_aff._bronni','Polymorphites?_apenninicus','Polymorphites?_bronni','Polymorphites?_flexicostatus','Polymorphites?_pseudodubari','Polymorphites_polymorphus','Polymorphites_rutilans','Prodactylioceras_aurigeriense','Prodactylioceras_davoei','Prodactylioceras_rectiradiatum','Pseudophricodoceras_caprariforme','Pseudophricodoceras_dayiforme','Pseudoskirroceras_mastodon','Radstockiceras_buvigneri','Radstockiceras_complanosum','Radstockiceras_pseudosaemanni','Radstockiceras_wiltshieri','Reynesocoeloceras_aegrum','Reynesocoeloceras_incertum','Reynesocoeloceras_indunense','Reynesocoeloceras_obesum','Reynesocoeloceras_praeincertum','Reynesocoeloceras_subcrassum','Sinuiceras_planulatum','Sinuiceras_sp._nov.','Sphaenoacanthites_costotuberculatum','Spiniclaviceras_spirale','Tetraspidoceras_evolutum','Tetraspidoceras_quadrarmatum','Tragophylloceras_carinatum','Tragophylloceras_ibex','Tragophylloceras_loscombi','Tragophylloceras_numismale','Tragophylloceras_undulatum','Tropidoceras_calliplocum','Tropidoceras_demonense','Tropidoceras_densicosta','Tropidoceras_erythraeum','Tropidoceras_flandrini','Tropidoceras_masseanum','Tropidoceras_mediterraneum','Tropidoceras_obtusum','Tropidoceras_orientale','Tropidoceras_semilaevis','Tropidoceras_stahli','Tropidoceras_stahliforme','Tropidoceras_sulcatus','Tropidoceras_zitteli','Tropidoceras_zitteli_sensu_AM','Uptonia?_juraphyllitoides','Uptonia?_sp._nov','Uptonia_confusa','Uptonia_jamesoni','Uptonia_lata','Vicininodiceras_gollingense','Vicininodiceras_simplicicosta','Villania_callomoni','Villania_densilobata','Zaghouanites_arcanum','Zamaiceras_carinatum','Zamaiceras_mangoldi','Zetoceras_iudicariense_sensu_GM','Zetoceras_zetes']
def get_taxa_names(): return taxa_names
