# django-bowl
bowling-kata in Django

## Install Docker!

Build Image
```
cd bowling
docker build -t py-bowling .

```

Run Image
```
docker run -it --rm -p 3000:8080 -p 2222:22  py-bowling

```

Login to Image
```
docker exec -it $(docker ps | grep py-bowling | awk '{print $1}') /bin/bash

#windows users: docker ps - copy image ID - 
docker exec -it DOCKERID /bin/bash
```

run tests
```
# activate virtualenv
root@02fca4c04821:/var/app# source bin/activate
root@02fca4c04821:/var/app# ./manage.py test
Creating test database for alias 'default'...
F
======================================================================
FAIL: test_gutter_game (score.tests.BowlingTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/var/app/bowling/score/tests.py", line 15, in test_gutter_game
    self.assertEqual(game.score(), 0)
AssertionError: 0 != -1

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
Destroying test database for alias 'default'...
```



open presentation.md ( http://aheld.github.io/bowling-score/ ) in a browser for step by step directions

##No reading ahead!
