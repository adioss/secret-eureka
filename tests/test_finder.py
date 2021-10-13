import unittest

from unconcealment import finder


class DefaultFinderTestCase(unittest.TestCase):
    """ Test module 'finder' """

    def test_contains_aws_key_pattern(self):
        """ test ex: AKIAU2XNOFEKTULFCVBA  """
        # Given
        tests = [
            {
                'value': 'test',
                'expected': None
            },
            {
                'value': 'AKIA',
                'expected': None
            },
            {
                'value': ' AKIAJJBR3C4RPHOVBYCV ',
                'expected': 'AKIAJJBR3C4RPHOVBYCV'
            },
            {
                'value': 'tototo AKIAtesttesttesttest ',
                'expected': 'AKIAtesttesttesttest'
            },
            {
                'value': 'ENV AWS_ACCESS_KEY_ID=AKIAJQGZRV7GX7CFXFUB',
                'expected': 'AKIAJQGZRV7GX7CFXFUB'
            },
            {
                'value': ' TOTOJJBR3C4YPHOVBYCV ',
                'expected': None
            },
            {
                'value': 'ENV MANPATH=/build//share/man:',
                'expected': None
            }
        ]
        for tested in tests:
            # When
            result = finder.extract_secret(tested['value'], finder.SecretPattern.AWS_KEY)
            # Then
            self.assertEqual(tested['expected'], result, f"Failed: {tested['value']}")

    def test_contains_aws_credential_file_pattern(self):
        """ test """
        # Given
        tests = [
            {'value': 'in /root/.aws/credential ', 'expected': None},
            {'value': 'in /root/.aws/credentials ', 'expected': 'in /root/.aws/credentials'}
        ]
        for tested in tests:
            # When
            result = finder.extract_secret(tested['value'], finder.SecretPattern.CREDENTIAL_FILE)
            # Then
            self.assertEqual(tested['expected'], result, f"Failed: {tested['value']}")

    def test_contains_aws_secret_pattern(self):
        """ test """
        # Given
        tests = [
            {
                'value': '/bin/sh -c curl -SLO "http://resin-packages.s3.amazonaws.com/resin-xbuild/v1.0.0/resin'
                         '-xbuild1.0.0.tar.gz  && rm "resin-xbuild1.0.0.tar.gz"   && chmod +x resin-xbuild   && mv '
                         'resin-xbuild /usr/bin   && ln -sf resin-xbuild /usr/bin/cross-build-start   && ln -sf '
                         'resin-xbuild /usr/bin/cross-build-end',
                'expected': None
            },
            {
                'value': 'tototo bFIiK2Ta5Dd3MEPJcnXzbJb01yRByRnrWMAvLpMa test ',
                'expected': None
            },
            {
                'value': 'ADD file:093f0723fa46f6cdbd6f7bd146448bb70ecce54254c35701feeceb956414622f in ',
                'expected': None
            },
            {
                'value': 'add dir:093f0723fa46f6cdbd6f7bd146448bb70ecce54254c35701feeceb956414622f in ',
                'expected': None
            },
            {
                'value': ' ENV ANOTHERNAME_SECRET_ACCESS_KEY=bFIiK2Ta5Dd3REPJcnXzbJb01yRByZnrWMAvLpMa',
                'expected': None
            },
            {
                'value': ' ENV AWS_SECRET_ACCESS_KEY=bFIiK2Ta5Dd3REPJcnXzbJb01yRByZnrWMAvLpMa',
                'expected': 'bFIiK2Ta5Dd3REPJcnXzbJb01yRByZnrWMAvLpMa'
            },
            {
                'value': ' ENV AWS_SECRET_ACCESS_KEY=4FcmDrL8tJ7jx8poyV0L5GOVqabM/Mk6wBHQREOH',
                'expected': '4FcmDrL8tJ7jx8poyV0L5GOVqabM/Mk6wBHQREOH'
            },
            {
                'value': 'tototo aws bFIiK2Ta5Dd3MEPJcnXzbJb01yRByZnrWMAvLpMa test ',
                'expected': 'bFIiK2Ta5Dd3MEPJcnXzbJb01yRByZnrWMAvLpMa'},
            {
                'value': 'https://apk.corretto.aws/amazoncorretto.rsa.pub && '
                         'SHA_SUM=\"6cfdf08be09f32ca298e2d5bd4a359ee2b275765c09b56d514624bf831eafb91',
                'expected': None
            },
        ]
        for tested in tests:
            # When
            result = finder.extract_secret(tested['value'], finder.SecretPattern.AWS_SECRET)
            # Then
            self.assertEqual(tested['expected'], result, f"Failed: {tested['value']}")

    def test_contains_github_key_pattern(self):
        """ test """
        # Given
        tests = [
            {'value': 'titi ghp_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa123456 tutu ',
             'expected': 'ghp_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa123456'}
        ]
        for tested in tests:
            # When
            result = finder.extract_secret(tested['value'], finder.SecretPattern.GITHUB_KEY)
            # Then
            self.assertEqual(tested['expected'], result, f"Failed: {tested['value']}")

    def test_contains_azure_client_secret_pattern(self):
        """ test """
        # Given
        tests = [
            {
                'value': 'ENV AZURE_ID=c35ba882-b5ed-405f-b929-49e8d8abd3f6 test',
                'expected': 'c35ba882-b5ed-405f-b929-49e8d8abd3f6'
            },
            {
                'value': 'ENV azure_id=c35ba882-b5ed-405f-b929-49e8d8abd3f6',
                'expected': 'c35ba882-b5ed-405f-b929-49e8d8abd3f6'
            },
            {
                'value': 'data before ENV azure_id=c35ba882-b5e4-405f-b929-39e8d8abd3f6 data after',
                'expected': 'c35ba882-b5e4-405f-b929-39e8d8abd3f6'
            },
            {
                'value': ' aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa ',
                'expected': None
            },
            {
                'value': 'ENV AZURE_ID=a882-b5ed-405f-b929-39e4d8abd3f6',
                'expected': None
            },
            {
                'value': 'ENV WEBSITE_ID=c35ba882-b5ed-405f-b929-49e8d8abd3f6',
                'expected': None
            },
            {
                'value': '854600d3-f5d9-45d7-9ff2-17d851f2831a',
                'expected': None
            },
            {
                'value': '{"digest": $url = \'https://download.microsoft.com/download/6/A/A/6AA4EDFF-645B-58C5-81CC'
                         '-ED5963AEAD48/vc_redist.x64.exe\'}',
                'expected': None
            },
        ]
        for tested in tests:
            # When
            result = finder.extract_secret(tested['value'], finder.SecretPattern.AZURE_CLIENT_ID)
            # Then
            self.assertEqual(tested['expected'], result, f"Failed: {tested['value']}")

    def test_contains_npm_token_pattern(self):
        """ test """
        # Given
        tests = [
            {
                'value': 'NPM_TOKEN=affa60d0-4fb5-4f88-9745-4c244e29372a',
                'expected': 'affa60d0-4fb5-4f88-9745-4c244e29372a'
            },
            {
                'value': '1 NPM_TOKEN=affa60d0-4fb5-4f88-9745-4c244e29372a /bin/sh -c apt-get update ',
                'expected': 'affa60d0-4fb5-4f88-9745-4c244e29372a'
            },
            {
                'value': '2 NPM_KEY=08a0a385-e6e2-4f3a-b96b-4eaf0a574d36 NPM_REPO=https://registry.npmjs.org/ ',
                'expected': '08a0a385-e6e2-4f3a-b96b-4eaf0a574d36'
            },
            {
                'value': '{"digest": $url = \'https://download.microsoft.com/download/6/A/A/6AA4EDFF-645B-48C5-81CC'
                         '-ED5963AEAD48/vc_redist.x64.exe\'}',
                'expected': None
            },
        ]
        for tested in tests:
            # When
            result = finder.extract_secret(tested['value'], finder.SecretPattern.NPM_TOKEN)
            # Then
            self.assertEqual(tested['expected'], result, f"Failed: {tested['value']}")

    def test_contains_heroku_key_pattern(self):
        """ test """
        # Given
        tests = [
            {
                'value': '/bin/sh -c apt-get install tmux && HEROKU_TOKEN=10211fef-fd5e-41ef-a49d-6b25e4df25d7 && sh',
                'expected': '10211fef-fd5e-41ef-a49d-6b25e4df25d7'
            }, {
                'value': '/bin/sh -c apt-get -y install tmux &&    apt-get install -y gnupg2 &&   '
                         ' curl https://cli-assets.heroku.com/install-ubuntu.sh | sh',
                'expected': None
            },
        ]
        for tested in tests:
            # When
            result = finder.extract_secret(tested['value'], finder.SecretPattern.HEROKU_KEY)
            # Then
            self.assertEqual(tested['expected'], result, f"Failed: {tested['value']}")

    def test_contains_pipy_key_pattern(self):
        """ test """
        # Given
        tests = [
            {
                'value': ' ENV PYPI_KEY = pypi-AgEIcHlwaS5vcmcCJGVhZWZjYmMfLTYzNDgtNDdhMi04NDFkLTkyOWNiODlkN2I3ZAACPnj'
                         'icGVybWlzc2lvbnMiOiB7InByb2plY3RaIjogWyJ1bmNvbmNlYWxtZW50Il19LCAidmVyc2lvbiI6IDF9AAAGIJcb-'
                         'aJdfJDLTHH0LEcyovcXfHk5i_zZtL3LeSxKpLZj ',
                'expected': 'pypi-AgEIcHlwaS5vcmcCJGVhZWZjYmMfLTYzNDgtNDdhMi04NDFkLTkyOWNiODlkN2I3ZAACPnj'
                            'icGVybWlzc2lvbnMiOiB7InByb2plY3RaIjogWyJ1bmNvbmNlYWxtZW50Il19LCAidmVyc2lvbiI6IDF9AAAGIJcb-'
                            'aJdfJDLTHH0LEcyovcXfHk5i_zZtL3LeSxKpLZj'
            },
        ]
        for tested in tests:
            # When
            result = finder.extract_secret(tested['value'], finder.SecretPattern.PIPY_KEY)
            # Then
            self.assertEqual(tested['expected'], result, f"Failed: {tested['value']}")

    def test_contains_twitter_key_pattern(self):
        """ test """
        # Given
        tests = [
            {
                'value': ' LABEL repo2docker.repo=https://github.com/robertICT/Webscrapping-Twitter',
                'expected': None
            },
        ]
        for tested in tests:
            # When
            result = finder.extract_secret(tested['value'], finder.SecretPattern.TWITTER_KEY)
            # Then
            self.assertEqual(tested['expected'], result, f"Failed: {tested['value']}")
