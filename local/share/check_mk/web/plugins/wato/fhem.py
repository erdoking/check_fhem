#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# Rules for configuring parameters of check fhem

#subgroup_networking =   _("Networking")

register_check_parameters(
    subgroup_environment,
    "fhem",
    _("FHEM"),
    Dictionary(
        title = _('FHEM parameters'),
        help = _('configure FHEM devices'),
        elements = [
            ## ####################################################
            ## Category common
            ## ####################################################
            ('common_params', Dictionary(
             title = "Common",
             required_keys = [],
             elements = [
              ## ----------------------------------------------------
              ## Sub-category Temperatur
              ## ----------------------------------------------------
              ('state_params', Dictionary(
               title = "Device state",
               required_keys = [],
               elements = [
                       ## Device state (reading)
                       ("var_state",
                         Alternative(
                            title = _('Decice state (r: state)'),
                            style = "dropdown",
                            allow_empty = False,
                            help = _("Check state of reading 'state' (default: ignore) "),
                            elements = [
                                FixedValue(
                                    'ok',
                                    totext = "ok",
                                    title = _("ok"),
                                ),
                                TextAscii(
                                    title = _("custom"),
                                    label = _("custom:"),
                                    size = 50,
                                ),
                           ]

                        )),
                       ## Device presence (reading)
                       ## maybe Sonoff specified?
                       ("var_presence",
                         Alternative(
                            title = _('Decice presence (r: presence)'),
                            style = "dropdown",
                            allow_empty = False,
                            help = _("Check state of reading 'presence' (default: present) "),
                            elements = [
                                FixedValue(
                                    'ignore',
#                                    totext = "ignore",
                                    title = _("ignore"),
                                ),
                                FixedValue(
                                    'present',
                                    totext = "present",
                                    title = _("present"),
                                ),
                                FixedValue(
                                    'absent',
                                    totext = "absent",
                                    title = _("absent"),
                                ),

                                TextAscii(
                                    title = _("custom"),
                                    label = _("custom:"),
                                    size = 50,
                                ),
                           ]

                        )),
               ],
              )),
              ## ----------------------------------------------------
              ## Sub-category Battery
              ## ----------------------------------------------------
              ('battery_params', Dictionary(
               title = "Battery state",
               required_keys = [],
               elements = [
                       ## Battery state
                       ("var_battery",
                         Alternative(
                            title = _('State of battery (r: battery'),
                            style = "dropdown",
                            allow_empty = False,
                            help = _("Check state of reading 'battery' (default: ok) "),
                            elements = [
                                FixedValue(
                                    'ignore',
                                    totext = "ignore",
                                    title = _("ignore"),
                                ),
                                TextAscii(
                                    title = _("custom"),
                                    label = _("custom:"),
                                    size = 50,
                                ),
                           ]

                        )),
                        ## Battery voltage
                        ( "level_batteryLevel_min",
                          Tuple(
                              title = _("Level for batterie voltage (r: batteryLevel)"),
                              help = _("You can adjust the levels before this service goes into warning/critical. Set to 0 to disable."),
                              elements = [
                                  Percentage(title = _("Warning at"), unit = "V", default_value = 2.3),
                                  Percentage(title = _("Critical at"), unit = "V", default_value = 2.1),
                              ]
                        )),

               ],
              )),

             ]
            )),

            ## ####################################################
            ## Category Climate
            ## ####################################################
            ('climate_params', Dictionary(
             title = "Climate",
             required_keys = [],
             elements = [
              ## ----------------------------------------------------
              ## Sub-category Temperature
              ## ----------------------------------------------------
              ('temperature_params', Dictionary(
               title = "Temperature",
               required_keys = [],
               elements = [
                       ## Temperature upper level
                       ( "level_temperature_max",
                          Tuple(
                              help = _("You can adjust the levels before this service goes into warning/critical. Set to 1000 to disable."),
                              title = _("Upper Levels (r: temperature)"),
                              elements = [
                                  Integer(title = _("Warning at"), unit = u"°C", default_value = 26),
                                  Integer(title = _("Critical at"), unit = u"°C", default_value = 30),
                              ]
                        )),
                        ## Temperature lower level
                        ( "level_temperature_min",
                          Tuple(
                              title = _("Lower Levels (r: temperature)"),
                              help = _("You can adjust the levels before this service goes into warning/critical. Set to -1000 to disable."),
                              elements = [
                                  Integer(title = _("Warning below"), unit = u"°C", default_value = 0),
                                  Integer(title = _("Critical below"), unit = u"°C", default_value = -10),
                              ]
                        )),
               ]
              )),
              ## ----------------------------------------------------
              ## Sub-category Humidity 
              ## ----------------------------------------------------
              ('humidity_params', Dictionary(
               title = "Humidity",
               required_keys = [],
               elements = [
                        ## Humidity upper level
                        ( "level_humidity_max",
                          Tuple(
                              help = _("You can adjust the levels before this service goes into warning/critical. Set to 1000 to disable."),
                              title = _("Upper levels (r: humidity)"),
                              elements = [
                                  Integer(title = _("Warning at"), unit = u"%", default_value = 70),
                                  Integer(title = _("Critical at"), unit = u"%", default_value = 80),
                              ]
                        )),
                        ## Humidity lower level
                        ( "level_humidity_min",
                          Tuple(
                              title = _("Lower levels (r: humidity)"),
                              help = _("You can adjust the levels before this service goes into warning/critical. Set to -1000 to disable."),
                              elements = [
                                  Integer(title = _("Warning below"), unit = u"%", default_value = 50),
                                  Integer(title = _("Critical below"), unit = u"%", default_value = 45),
                              ]
                        )),
               ]
              )),
              ## ----------------------------------------------------
              ## Sub-category dewpoint
              ## ----------------------------------------------------
              ('dewpoint_params', Dictionary(
               title = "Dewpoint",
               required_keys = [],
               elements = [
                        ## Dewpoint upper level
                        ( "level_dewpoint_max",
                          Tuple(
                              title = _("diff to temperatur"),
                              help = _("exp. 17°C [dewp] vs 20°C [temp] (r: dewpoint) "),
                              elements = [
                                  Integer(title = _("Warning below"), unit = u"°C", default_value = 3),
                                  Integer(title = _("Critical below"), unit = u"°C", default_value = 1),
                              ]
                        )),
                        ## ignore humidity
                        ("var_dewpoint_override",
                         Alternative(
                            title = _('ignore humidity (r: humidity+dewpoint)'),
                            style = "dropdown",
                            allow_empty = False,
                            help = _("don't alert humidity if dewpoint given. (default: true)"),
                            elements = [
                                FixedValue(
                                    'true',
                                    totext = "true",
                                    title = _("true"),
                                ),
                                FixedValue(
                                    'false',
                                    totext = "false",
                                    title = _("false"),
                                ),
                           ]
                        )),
               ]
              )),
             ],
            )),
            ## ####################################################
            ## Category Various 
            ## ####################################################
            ('various_params', Dictionary(
             title = "Various",
             help = _("everything else ..."),
             elements = [
              ## ----------------------------------------------------
              ## Sub-category Speedtest 
              ## ----------------------------------------------------
              ('speedtest_params', Dictionary(
               title = "Speedtest",
               required_keys = [],
               elements = [
                        ## speedtest download
                        ( "level_download_min",
                          Tuple(
                              title = _("Level for speedtest download "),
                              help = _("You can adjust the levels before this service goes into warning/critical. Set to 0 to disable. (r: download)"),
                              elements = [
                                  Percentage(title = _("Warning at"), unit = "Mbit/s", default_value = 10.0),
                                  Percentage(title = _("Critical at"), unit = "Mbit/s", default_value = 8.0),
                              ]
                        )),
                        ## speedtest upload
                        ( "level_upload_min",
                          Tuple(
                              title = _("Level for speedtest upload"),
                              help = _("You can adjust the levels before this service goes into warning/critical. Set to 0 to disable. (r: upload)"),
                              elements = [
                                  Percentage(title = _("Warning at"), unit = "Mbit/s", default_value = 1.5),
                                  Percentage(title = _("Critical at"), unit = "Mbit/s", default_value = 1.0),
                              ]
                        )),
                        ## speedtest ping
                        ( "level_ping_max",
                          Tuple(
                              title = _("Level for speedtest ping"),
                              help = _("You can adjust the levels before this service goes into warning/critical. Set to 0 to disable. (r: ping)"),
                              elements = [
                                  Integer(title = _("Warning at"), unit = "ms", default_value = 100),
                                  Integer(title = _("Critical at"), unit = "ms", default_value = 150),
                              ]
                        )),
               ]
              )),
             ],
            )),
            ## ####################################################
            ## Category Device types
            ## ####################################################
            ('devicetypes_params', Dictionary(
             title = "Device types",
             required_keys = [],
             elements = [
              ## ----------------------------------------------------
              ## Sub-category Light 
              ## ----------------------------------------------------
              ('light_params', Dictionary(
               title = "Light",
               required_keys = [],
               elements = [
                       ("var_RGB_color",
                         Alternative(
                            title = _('RGB color (r: RGB)'),
                            style = "dropdown",
                            allow_empty = False,
                            help = _("Check state of reading 'RGB' (without #)"),
                            elements = [
                                FixedValue(
                                    'FFFFFF',
                                    totext = "white",
                                    title = _("white"),
                                ),
                                TextAscii(
                                    title = _("custom"),
                                    label = _("custom:"),
                                    size = 6,
                                ),
                           ]

                        )),
                       ("var_brightness",
                         Alternative(
                            title = _('light brightness (r: brightness)'),
                            style = "dropdown",
                            allow_empty = False,
                            help = _("Check state of reading 'brightness' (default: ignore) "),
                            elements = [
                                FixedValue(
                                    '100',
                                    totext = "100%",
                                    title = _("100%"),
                                ),
                                FixedValue(
                                    '0',
                                    totext = "0%",
                                    title = _("0%"),
                                ),
                                TextAscii(
                                    title = _("custom"),
                                    label = _("custom:"),
                                    size = 3,
                                ),
                           ]

                        )),

               ]
              )),
              ## ----------------------------------------------------
              ## Sub-category Contact sensor
              ## ----------------------------------------------------
              ('contactsensor_params', Dictionary(
               title = "Contact sensor",
               required_keys = [],
               elements = [
                        ("var_contact",
                         Alternative(
                            title = _('Contact state (r: contact)'),
                            style = "dropdown",
                            allow_empty = False,
                            help = _("Check state of reading 'contact' (default: ignore) "),
                            elements = [
                                FixedValue(
                                    'open',
                                    totext = "open",
                                    title = _("open"),
                                ),
                                FixedValue(
                                    'closed',
                                    totext = "closed",
                                    title = _("closed"),
                                ),
                                TextAscii(
                                    title = _("custom"),
                                    label = _("custom:"),
                                    size = 50,
                                ),
                           ]
                       )),

               ]
              )),           

             ],
            )),
            ## ####################################################
            ## Category Manufacturer
            ## ####################################################
            ('manufacturer_params', Dictionary(
             title = "Manufacturer",
             help = _("Manufacturer specific parameter"),
             elements = [
              ## ----------------------------------------------------
              ## Sub-category HomeMatic
              ## ----------------------------------------------------
              ('homematic_params', Dictionary(
               title = "HomeMatic",
               help = _("HomeMatic specific parameter"),
               allow_empty = False,
               elements = [
               ("var_btnLock",
                 Alternative(
                    title = _('btnLock state'),
                    style = "dropdown",
                    allow_empty = False,
                    help = _("Check state of reading 'btnLock' (default: ignore) "),
                    elements = [
                        FixedValue(
                            'on',
                            totext = "on",
                            title = _("on"),
                        ),
                        FixedValue(
                            'off',
                            totext = "off",
                            title = _("off"),
                        ),
                        TextAscii(
                            title = _("custom"),
                            label = _("custom:"),
                            size = 50,
                        ),
                   ]

                )),
               ("var_globalBtnLock",
                 Alternative(
                    title = _('globalBtnLock state'),
                    style = "dropdown",
                    allow_empty = False,
                    help = _("Check state of reading 'globalBtnLock' [default: ignore] (r: globalBtnLock) "),
                    elements = [
                        FixedValue(
                            'on',
                            totext = "on",
                            title = _("on"),
                        ),
                        FixedValue(
                            'off',
                            totext = "off",
                            title = _("off"),
                        ),
                        TextAscii(
                            title = _("custom"),
                            label = _("custom:"),
                            size = 50,
                        ),
                   ]

                )),
               ("var_modusBtnLock",
                 Alternative(
                    title = _('modusBtnLock state'),
                    style = "dropdown",
                    allow_empty = False,
                    help = _("Check state of reading 'modusBtnLock' [default: ignore] (r: modusBtnLock) "),
                    elements = [
                        FixedValue(
                            'on',
                            totext = "on",
                            title = _("on"),
                        ),
                        FixedValue(
                            'off',
                            totext = "off",
                            title = _("off"),
                        ),
                        TextAscii(
                            title = _("custom"),
                            label = _("custom:"),
                            size = 50,
                        ),
                   ]

                )),
                ("var_controlMode",
                 Alternative(
                    title = _('Control Mode'),
                    style = "dropdown",
                    allow_empty = False,
                    help = _("Check current control mode. (default: ignore)"),
                    elements = [
                        FixedValue(
                            'auto',
                            totext = "auto",
                            title = _("auto"),
                        ),
                        FixedValue(
                            'manual',
                            totext = "manual",
                            title = _("manual"),
                        ),
                        FixedValue(
                            'boost',
                            totext = "boost",
                            title = _("boost"),
                        ),
                        FixedValue(
                            'day',
                            totext = "day",
                            title = _("day"),
                        ),
                        FixedValue(
                            'night',
                            totext = "night",
                            title = _("night"),
                        ),

                        TextAscii(
                            title = _("custom"),
                            label = _("custom:"),
                            size = 50,
                        ),
                   ]
                )),

               ]
              )),

             ],
            )),


        ],
#        required_keys = [ 'service_description', 'imap_parameters' ]
    ),
    TextAscii(
        title = _("fhem device"),
        help = _("Specify the name of the FHEM device, i.e. <tt>eg.bad.heizung</tt>"),
        allow_empty = False,
        default_value = 0,
    ),
    "dict",
)


