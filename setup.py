import setuptools

setuptools.setup(
        name = 'gector',
        packages = setuptools.find_packages(),
        entry_points = {
            'console_scripts':[
                'gector_train = train:main',
                ]},)
