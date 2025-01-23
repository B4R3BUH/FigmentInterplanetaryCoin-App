def check_buttons_creating(button_creating_value, earn_button_created, boosts_button_created, frens_button_created, airdrop_button_created, icons_button_created, settings_button_created):
    dict = {
        'earn': earn_button_created,
        'boosts': boosts_button_created,
        'frens': frens_button_created,
        'airdrop': airdrop_button_created,
        'icons': icons_button_created,
        'settings': settings_button_created
    }

    return dict[button_creating_value]