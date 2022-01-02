from classes import NotPrivate, _Private

test_private = _Private('puppy')


test_public = NotPrivate('tommy')              # public class ko object create gareko
test_public.display()                          # public method lai tw sajilai access garna sakincha
test_public._display()                         # public class ko private method lai pani access garna sakincha
