icon_dict = {
        1: [
            {
                'icon_db_value': 'skin_1',
                'icon_name': '"F.I.C Default"',
                'icon_logo': 'data/Icons/skin_1.png',
                'price': 'Выдается на старте',
                'tokens': 0
            }
        ],
        2: [
            {
                'icon_db_value': 'skin_1_plus',
                'icon_name': '"F.I.C Enchanted"',
                'icon_logo': 'data/Icons/skin_2.png',
                'price': '70K',
                'tokens': 70000
            }
        ],
        3: [
            {
                'icon_db_value': 'skin_2',
                'icon_name': '"Меркурий Ретроград"',
                'icon_logo': 'data/Icons/skin_3.png',
                'price': '50K',
                'tokens': 50000
            }
        ],
        4: [
            {
                'icon_db_value': 'skin_3',
                'icon_name': '"Венера"',
                'icon_logo': 'data/Icons/skin_4.png',
                'price': '75K',
                'tokens': 75000
            }
        ],
        5: [
            {
                'icon_db_value': 'skin_4',
                'icon_name': '"Нашинские"',
                'icon_logo': 'data/Icons/skin_5.png',
                'price': '100K',
                'tokens': 100000
            }
        ],
        6: [
            {
                'icon_db_value': 'skin_5',
                'icon_name': '"Вечный спутник"',
                'icon_logo': 'data/Icons/skin_6.png',
                'price': '125K',
                'tokens': 125000
            }
        ],
        7: [
            {
                'icon_db_value': 'skin_6',
                'icon_name': '"Марс Ретроград"',
                'icon_logo': 'data/Icons/skin_7.png',
                'price': '150K',
                'tokens': 150000
            }
        ],
        8: [
            {
                'icon_db_value': 'skin_7',
                'icon_name': '"Газовый гигант"',
                'icon_logo': 'data/Icons/skin_8.png',
                'price': '200K',
                'tokens': 200000
            }
        ],
        9: [
            {
                'icon_db_value': 'skin_8',
                'icon_name': '"Кольцевая"',
                'icon_logo': 'data/Icons/skin_9.png',
                'price': '250K',
                'tokens': 250000
            }
        ],
        10: [
            {
                'icon_db_value': 'skin_9',
                'icon_name': '"Вторая кольцевая"',
                'icon_logo': 'data/Icons/skin_10.png',
                'price': '300K',
                'tokens': 300000
            }
        ],
        11: [
            {
                'icon_db_value': 'skin_10',
                'icon_name': '"Камчатская планета"',
                'icon_logo': 'data/Icons/skin_11.png',
                'price': '350K',
                'tokens': 350000
            }
        ],
        12: [
            {
                'icon_db_value': 'skin_11',
                'icon_name': '"Дисквалифицирован"',
                'icon_logo': 'data/Icons/skin_12.png',
                'price': '50K',
                'tokens': 50000
            }
        ],
        13: [
            {
                'icon_db_value': 'skin_12',
                'icon_name': '"Crystal Castles"',
                'icon_logo': 'data/Icons/skin_13.png',
                'price': '400K',
                'tokens': 400000
            }
        ],
        14: [
            {
                'icon_db_value': 'skin_13',
                'icon_name': '"Пельмень Сатурна"',
                'icon_logo': 'data/Icons/skin_14.png',
                'price': '1M',
                'tokens': 1000000
            }
        ],
        15: [
            {
                'icon_db_value': 'skin_14',
                'icon_name': '"Дружелюбный великан"',
                'icon_logo': 'data/Icons/skin_15.png',
                'price': 'Нужно пригласить друга в FIC',
                'tokens': 0
            }
        ]
    }

boosts_dict = {
    'boost1': [
        {
            'boost_db_value': 'boost_coin_per_tap',
            'level': [
                {
                    1: [
                        {
                            'tap': 1,
                            'price_boost1': '5K',
                            'buy_boost1': 5000
                        }
                    ],
                    2: [
                        {
                            'tap': 2,
                            'price_boost1': '20K',
                            'buy_boost1': 20000
                        }
                    ],
                    3: [
                        {
                            'tap': 4,
                            'price_boost1': '80K',
                            'buy_boost1': 80000
                        }
                    ],
                    4: [
                        {
                            'tap': 8,
                            'price_boost1': '160K',
                            'buy_boost1': 160000
                        }
                    ],
                    5: [
                        {
                            'tap': 16,
                        }
                    ]
                }
            ],
            'description': 'Этот буст является множителем\nочков FIC за 1 тап по монете.\nОт Кондиций отнимается такое значение,\nсколько вы получаете очков FIC за тап'
        }
    ],

    'boost2': [
        {
            'boost_db_value': 'boost_charge_full',
            'level': [
                {
                    1: [
                        {
                            'conditions_full': 25000,
                            'price_boost2': '5K',
                            'buy_boost2': 5000,
                            'lvl': 1
                        }
                    ],
                    2: [
                        {
                            'conditions_full': 30000,
                            'price_boost2': '10K',
                            'buy_boost2': 10000,
                            'lvl': 2
                        }
                    ],
                    3: [
                        {
                            'conditions_full': 35000,
                            'price_boost2': '20K',
                            'buy_boost2': 20000,
                            'lvl': 3
                        }
                    ],
                    4: [
                        {
                            'conditions_full': 40000,
                            'price_boost2': '40K',
                            'buy_boost2': 40000,
                            'lvl': 4
                        }
                    ],
                    5: [
                        {
                            'conditions_full': 45000,
                            'price_boost2': '80K',
                            'buy_boost2': 80000,
                            'lvl': 5
                        }
                    ],
                    6: [
                        {
                            'conditions_full': 50000,
                            'price_boost2': '160K',
                            'buy_boost2': 160000,
                            'lvl': 6
                        }
                    ],
                    7: [
                        {
                            'conditions_full': 60000,
                            'lvl': 7
                        }
                    ]
                }
            ],
            'description': 'Этот буст является\nувеличением значения Кондиций.\nЧем больше Кондиций, тем больше\nможно тапать за промежуток времени'
        }
    ]
}

passive_farm_setup_dict = {
    'setup1': {
        'setup_db_value': 'setup_time_until_getting',
        'level': [
            {
                1: [
                    {
                        'time_until': 4,
                        'price_setup1': '25K',
                        'buy_setup1': 25000,
                    }
                ],
                2: [
                    {
                        'time_until': 6,
                        'price_setup1': '50K',
                        'buy_setup1': 50000,
                    }
                ],
                3: [
                    {
                        'time_until': 8,
                        'price_setup1': '75K',
                        'buy_setup1': 75000,
                    }
                ],
                4: [
                    {
                        'time_until': 12,
                        'price_setup1': '100K',
                        'buy_setup1': 100000,
                    }
                ],
                5: [
                    {
                        'time_until': 24,
                        'price_setup1': '150K',
                        'buy_setup1': 150000,
                    }
                ]
            }
        ],
        'description': 'Этот сетап является\nувеличением количества времени\nдо сбора накопленных токенов.\nЧем больше Промежуток времени,\nтем дольше можно не собирать\nнакопленные токены'
    },
    'setup2': {
        'setup_db_value': 'setup_tokens_getting',
        'level': [
            {
                1: [
                    {
                        'many_tokens': 25000,
                        'price_setup2': '150K',
                        'buy_setup2': 150000,
                    }
                ],
                2: [
                    {
                        'many_tokens': 50000,
                        'price_setup2': '200K',
                        'buy_setup2': 200000,
                    }
                ],
                3: [
                    {
                        'many_tokens': 75000,
                        'price_setup2': '500K',
                        'buy_setup2': 75000,
                    }
                ],
                4: [
                    {
                        'many_tokens': 100000,
                        'price_setup2': '1M',
                        'buy_setup2': 1000000,
                    }
                ],
                5: [
                    {
                        'many_tokens': 150000,
                        'price_setup2': '2M',
                        'buy_setup2': 2000000,
                    }
                ]
            }
        ],
        'description': 'Этот сетап является\nувеличением количества токенов\nза 1ч во время Пассивного фарма.\nЧем больше Доступных токенов,\nтем больше можно собрать\nза один промежуток фарма'
    }
}

icon_values_dict = {
    1: 'data/Icons/skin_1.png',
    2: 'data/Icons/skin_2.png',
    3: 'data/Icons/skin_3.png',
    4: 'data/Icons/skin_4.png',
    5: 'data/Icons/skin_5.png',
    6: 'data/Icons/skin_6.png',
    7: 'data/Icons/skin_7.png',
    8: 'data/Icons/skin_8.png',
    9: 'data/Icons/skin_9.png',
    10: 'data/Icons/skin_10.png',
    11: 'data/Icons/skin_11.png',
    12: 'data/Icons/skin_12.png',
    13: 'data/Icons/skin_13.png',
    14: 'data/Icons/skin_14.png',
}