# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

# If this file is changed in development, the development server will
# have to be manually restarted because changes will not be noticed
# immediately.

# from inmates.jims_init import init_jims

SECRET_KEY = "6@6x4y$jd@jq6(-t9t#tqq6&jgg93bi128%+0%8m2tj5-p3+$g"
NEVERCACHE_KEY = "m2v1wk(=mw#5cu5)erl-^(3zgz%rh)lb(b8e0er6#i#m559e^0"

DEBUG = True
INITIAL_BUILD = True

#
# BLOCKS_PER_PRISON= 10
# CELLS_PER_BLOCK = 100
# PRISONS = [
#     ("San Diego Central Jail", "(619) 610-1647"),
#     ("Las Colinas Detention & Reentry Facility", "(619) 402-1312"),
#     ("Vista Detention Facility", "(760) 936-0014"),
#     ("George Bailey Detention Facility", "(619) 210-0385"),
#     ("South Bay Detention Facility", "(619) 213-1433"),
#     ("East Mesa Reentry Facility", "(619) 210-0334"),
#     ("Facility 8 Detention Facility", "(619) 210-0327")
# ]
#
# if INITIAL_BUILD:
#     init_jims(PRISONS, BLOCKS_PER_PRISON, CELLS_PER_BLOCK)
#

# Make these unique, and don't share it with anybody.


DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}




###################
# DEPLOY SETTINGS #
###################

# Domains for public site
# ALLOWED_HOSTS = [""]

# These settings are used by the default fabfile.py provided.
# Check fabfile.py for defaults.

# FABRIC = {
#     "DEPLOY_TOOL": "rsync",  # Deploy with "git", "hg", or "rsync"
#     "SSH_USER": "",  # VPS SSH username
#     "HOSTS": [""],  # The IP address of your VPS
#     "DOMAINS": ALLOWED_HOSTS,  # Edit domains in ALLOWED_HOSTS
#     "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
#     "LOCALE": "en_US.UTF-8",  # Should end with ".UTF-8"
#     "DB_PASS": "",  # Live database password
#     "ADMIN_PASS": "",  # Live admin user password
#     "SECRET_KEY": SECRET_KEY,
#     "NEVERCACHE_KEY": NEVERCACHE_KEY,
# }
