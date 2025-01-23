def get_sizes(screen_width, get_size_value):
    dict = {}

    if screen_width >= 1200:
        dict = {
            'coin': 1100,
            'label_font': 74,
            'button_menu': screen_width / 4.5,
            'boost_label_font': 0,
            'settings_label_font_size': 0,
            'boost_button_sizes': 0,
            'label_frens_font': 0,
            'airdrop_button_sizes': 0,
            'all_icons_button_size': 0,
            'more_icon_button_sizes': 0,
            'more_icon_font_size': 0,
            'more_icon_screen_box_layout_pos_y': .9,
            'airdrop_box_layout_center_y': .9,
            'frens_layout_spacing': 250,
            'passive_farm_button_size': screen_width / 5,
            'boost_layout_spacing': 570,
            'frens_layout_spacing_no_frens': 350,
            'about_starting_layout_spacing': 210,
            'about_starting_layout_center_y': .55,
            'textinput_font_size': 40,
            'passive_farm_explanation_buttons_width': 380,
            'passive_farm_explanation_buttons_height': 100,
            'horizontal_rectangle_buttons_width': 500,
            'horizontal_rectangle_buttons_height': 145
        }
        dict['boost_label_font'] = dict['label_font'] / 2.5
        dict['settings_label_font_size'] = dict['label_font'] / 2.8
        dict['label_frens_font'] = dict['label_font'] / 2
        dict['more_icon_font_size'] = dict['label_font'] / 2.4
        dict['boost_button_sizes'] = dict['coin'] / 2.4
        dict['airdrop_button_sizes'] = dict['coin'] / 1.2
        dict['all_icons_button_size'] = dict['coin'] / 4.25
        dict['more_icon_button_sizes'] = dict['coin'] / 1.2

    elif screen_width > 1010 and screen_width < 1200:
        dict = {
            'coin': 980,
            'label_font': 60,
            'button_menu': screen_width / 4.5,
            'boost_label_font': 0,
            'settings_label_font_size': 0,
            'boost_button_sizes': 0,
            'label_frens_font': 0,
            'airdrop_button_sizes': 0,
            'all_icons_button_size': 0,
            'more_icon_button_sizes': 0,
            'more_icon_font_size': 0,
            'more_icon_screen_box_layout_pos_y': .9,
            'airdrop_box_layout_center_y': .9,
            'frens_layout_spacing': 180,
            'passive_farm_button_size': screen_width / 4.5,
            'boost_layout_spacing': 470,
            'frens_layout_spacing_no_frens': 320,
            'about_starting_layout_spacing': 190,
            'about_starting_layout_center_y': .55,
            'textinput_font_size': 36,
            'passive_farm_explanation_buttons_width': 380,
            'passive_farm_explanation_buttons_height': 100,
            'horizontal_rectangle_buttons_width': 380,
            'horizontal_rectangle_buttons_height': 100
        }
        dict['boost_label_font'] = dict['label_font'] / 2
        dict['settings_label_font_size'] = dict['label_font'] / 2
        dict['label_frens_font'] = dict['label_font'] / 1.5
        dict['more_icon_font_size'] = dict['label_font'] / 2.2
        dict['boost_button_sizes'] = dict['coin'] / 2.25
        dict['airdrop_button_sizes'] = dict['coin'] / 1.2
        dict['all_icons_button_size'] = dict['coin'] / 4
        dict['more_icon_button_sizes'] = dict['coin'] / 1.4

    elif screen_width <= 1000:
        dict = {
            'coin': 620,
            'label_font': 36,
            'button_menu': screen_width / 4,
            'boost_label_font': 0,
            'settings_label_font_size': 0,
            'boost_button_sizes': 0,
            'label_frens_font': 0,
            'airdrop_button_sizes': 0,
            'all_icons_button_size': 0,
            'more_icon_button_sizes': 0,
            'more_icon_font_size': 0,
            'more_icon_screen_box_layout_pos_y': .9,
            'airdrop_box_layout_center_y': .9,
            'frens_layout_spacing': 90,
            'passive_farm_button_size': screen_width / 4,
            'boost_layout_spacing': 300,
            'frens_layout_spacing_no_frens': 110,
            'about_starting_layout_spacing': 70,
            'about_starting_layout_center_y': .55,
            'textinput_font_size': 26,
            'passive_farm_explanation_buttons_width': 225,
            'passive_farm_explanation_buttons_height': 70,
            'horizontal_rectangle_buttons_width': 225,
            'horizontal_rectangle_buttons_height': 70
        }
        dict['boost_label_font'] = dict['label_font'] / 1.8
        dict['settings_label_font_size'] = dict['label_font'] / 2
        dict['label_frens_font'] = dict['label_font'] / 1.7
        dict['more_icon_font_size'] = dict['label_font'] / 1.3
        dict['boost_button_sizes'] = dict['coin'] / 2.2
        dict['airdrop_button_sizes'] = dict['coin'] / 1.1
        dict['all_icons_button_size'] = dict['coin'] / 4
        dict['more_icon_button_sizes'] = dict['coin'] / 1.6

    returning_value = dict[get_size_value]
    return returning_value