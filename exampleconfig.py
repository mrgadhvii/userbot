from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 24808705
    API_HASH = "adf3a113ab32bb2792338477f156dc86"
    # the name to display in your alive message
    ALIVE_NAME = "Jaydevv"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "Your value"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOKEBuzMu9njHLd6127hI1j3NrTf4P4EQ4wdgyYA74AYZyBXTyVKMhYHTx3C710TCd8ntOad-4_PLSOJkNtSq3G9vOh7Ik0xnnpoObUogKtGvPfHHVCmIp31sA0-FdiEi2R8EoXF5RCnbBbJ8BHblGMTDfq6w4kHUWhAGK9o_2AEyc0pjI7wZwgUeYDo6BimkUfKKXeK1Cg65PGdsY3DUjN6bTCX_772EwQatk6kVJE5asK1EFSbRPVGMWFkURtAG6cKURp98Hu6Na9PkC2ZimNMS8gP8U7EjFHJbC7JhJ4fJnuyLDJI8swi0Jc48b6jbmum_zPTQRbxSA-6L0cbVPGOEhR4="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "8015052876:AAEi65xgC7XzKRcn9hKGBY48wDlFrUDQuUY"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1002327175372
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "False"
