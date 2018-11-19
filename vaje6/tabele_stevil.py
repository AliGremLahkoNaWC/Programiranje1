# =============================================================================
# Tabele števil
# =====================================================================@017382=
# 1. podnaloga
# Premisli, kaj počne spodaj navedena funkcija. Žal je rezultat domače naloge
# študenta 1. letnika, ki še ne ve, da funkcija brez komentarjev ni preveč ...
# 
#        def funk(tab):
#            j = 0            
#            i = 0
#            d = len(tab)
#            while i < d:    
#                if tab[i] == 1:
#                    j += 1   
#                i += 2
#            return j        
# 
# Predelaj jo (kar pomeni tudi, da jo opremiš s komentarji, ustrezno popraviš
# imena spremenljivk ...) v funkcijo `prestej(n, tabelaSt)`, ki prešteje,
# kolikokrat se tabeli `tabelaSt` pojavi število `n`
# Na primer:
# 
#       >>> prestej(5,[2, 5, 12, 3, 5, 3, 12, 8, 12])
#       2
# =============================================================================
def prestej(n, tabelaSt):
    ''' Funkcija bo prestela kolikokrat se parameter n,
    pojavi v dani tabeli.'''
    i = 0 # indeks
    n_krat = 0
    while i < len(tabelaSt):
        if tabelaSt[i] == n:
            n_krat += 1
        i += 1
    return n_krat
# =====================================================================@017383=
# 2. podnaloga
# Napiši funkcijo `prestejSode(tab_st)`, ki v tabeli števil prešteje,
# kolikokrat se v tej tabeli pojavi sodo število. 
# Na primer:
# 
#       >>> prestejSode([2, 5, 12, 3, 5, 3, 12, 8, 12])
#       5
# =============================================================================
def prestejSode(tab_st):
    ''' Funkcija bo vrnila stevilo sodih stevil v tabeli.'''
    i = 0 # indeks
    sod = 0 # stevec sodih stevil
    while i < len(tab_st):
        if tab_st[i] % 2 == 0:
            sod += 1
        i += 1
    return sod
            
# =====================================================================@017384=
# 3. podnaloga
# Napiši funkcijo `prestejSodeLihe(tab_st)`, ki v tabeli števil prešteje,
# kolikokrat se v tej tabeli pojavi sodo število. Rezultat naj vrne v
# obliki para `(soda, liha)`
# Na primer:
# 
#       >>> prestejSodeLihe([2, 5, 12, 3, 5, 3, 12, 8, 12])
#       (5, 4)
# =============================================================================
def prestejSodeLihe(tab_st):
    ''' Funkcija bo vrnila stevilo sodih ter lihih stevil v tabeli.'''
    i = 0 # indeks
    sod = 0 # stevec sodih stevil
    lih = 0 # stevec lihih stevil
    while i < len(tab_st):
        if tab_st[i] % 2 == 0:
            sod += 1
        else:
            lih += 1
        i += 1
    return sod,lih
# =====================================================================@017385=
# 4. podnaloga
# Funkcija `tabMest(n,tab_st)`
# 
#      def tabMest(n, tab_st):
#          '''indeksi, kje se v tabeli pojavi n '''
#          i = 1
#          while i <= len(tab_st):    # potujemo po vseh indeksih tabele
#              if tab_st[i] == n:          # primerjamo ali je i-ti elt. enak n
#                  mesta.append([i])         # če pridemo do tega mesta, indeks dodamo k novi tabeli
#              i = i + 1
#          return mesta                   # vrne nam tabelo indeksov
# 
# naj bi vrnila tabelo vseh mest, na katerih se v tabeli števil pojavi
# število `n`. Mesta štejemo od 0 dalje! Na primer:
# 
#       >>> tabMest(12,[2, 5, 12, 3, 5, 3, 12, 8, 12])
#       [2, 6, 8]
# 
# Žal ne dela prav. Ima sintaktične in semantične napake. Popravi jo!
# =============================================================================
def tabMest(n, tab_st):
   '''indeksi, kje se v tabeli pojavi n '''
   i = 0
   mesta = []
   while i < len(tab_st):    # potujemo po vseh indeksih tabele
      if tab_st[i] == n:          # primerjamo ali je i-ti elt. enak n
          mesta.append(i)         # če pridemo do tega mesta, indeks dodamo k novi tabeli
      i = i + 1
   return mesta                   # vrne nam tabelo indeksov
# =====================================================================@017386=
# 5. podnaloga
# Funkcija `kolikoEnic(tab_celih)` naj vrne tabelo dolžine 10, kjer na mestu 
# `i` povemo, koliko je v tabeli `tab_celih` števil, ki imajo kot enice 
# vrednost `i`.
# Na primer:
# 
#       >>> kolikoEnic([1432, 32155, 12, 351, 12353, 1255, 2313, 12, 8, 112])
#       [0, 1, 4, 2, 0, 2, 0, 0, 1, 0]
# 
# saj v tabeli števil ni nobenega števila, ki bi imelo na mestu enic 0, je
# eno število (namreč 351), ki ima na mestu enic 1, 4 števila
# (1432, 12, 12 in 112), ki imajo na mestu enic 2 ....
# =============================================================================
def kolikoEnic(tab_celih):
    '''Funkcija bo vrnila seznam, ki bo povedal kolikokrat se stevila
    pojavijo na mestih enic, pri dani vrednosti (to je indeks). Torej,
    ce je indeks = 0, bo preveril kolikokrat se pojavi stevilo 0
    na mestu enic, za vsak element tabele.'''
    i1 = 0 # glavni stevec
    i2 = 0 # sekundarni stevec
    stevec = 0
    seznam = [] * 10
    while i1 < len(tab_celih):
        
        while i2 < len(tab_celih):
            if tab_celih[i2] % 10 == i1:
                stevec += 1
            i2 += 1
        seznam.append(stevec)
        stevec = 0
        i2 = 0
        i1 += 1
    return seznam




































































































# ============================================================================@

'Če vam Python sporoča, da je v tej vrstici sintaktična napaka,'
'se napaka v resnici skriva v zadnjih vrsticah vaše kode.'

'Kode od tu naprej NE SPREMINJAJTE!'


















































import json, os, re, sys, shutil, traceback, urllib.error, urllib.request


import io, sys
from contextlib import contextmanager

class VisibleStringIO(io.StringIO):
    def read(self, size=None):
        x = io.StringIO.read(self, size)
        print(x, end='')
        return x

    def readline(self, size=None):
        line = io.StringIO.readline(self, size)
        print(line, end='')
        return line

class Check:
    @staticmethod
    def has_solution(part):
        return part['solution'].strip() != ''

    @staticmethod
    def initialize(parts):
        Check.parts = parts
        for part in Check.parts:
            part['valid'] = True
            part['feedback'] = []
            part['secret'] = []
        Check.current_part = None
        Check.part_counter = None

    @staticmethod
    def part():
        if Check.part_counter is None:
            Check.part_counter = 0
        else:
            Check.part_counter += 1
        Check.current_part = Check.parts[Check.part_counter]
        return Check.has_solution(Check.current_part)

    @staticmethod
    def feedback(message, *args, **kwargs):
        Check.current_part['feedback'].append(message.format(*args, **kwargs))

    @staticmethod
    def error(message, *args, **kwargs):
        Check.current_part['valid'] = False
        Check.feedback(message, *args, **kwargs)

    @staticmethod
    def clean(x, digits=6, typed=False):
        t = type(x)
        if t is float:
            x = round(x, digits)
            # Since -0.0 differs from 0.0 even after rounding,
            # we change it to 0.0 abusing the fact it behaves as False.
            v = x if x else 0.0
        elif t is complex:
            v = complex(Check.clean(x.real, digits, typed), Check.clean(x.imag, digits, typed))
        elif t is list:
            v = list([Check.clean(y, digits, typed) for y in x])
        elif t is tuple:
            v = tuple([Check.clean(y, digits, typed) for y in x])
        elif t is dict:
            v = sorted([(Check.clean(k, digits, typed), Check.clean(v, digits, typed)) for (k, v) in x.items()])
        elif t is set:
            v = sorted([Check.clean(y, digits, typed) for y in x])
        else:
            v = x
        return (t, v) if typed else v

    @staticmethod
    def secret(x, hint=None, clean=None):
        clean = Check.get('clean', clean)
        Check.current_part['secret'].append((str(clean(x)), hint))

    @staticmethod
    def equal(expression, expected_result, clean=None, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get('clean', clean)
        actual_result = eval(expression, global_env)
        if clean(actual_result) != clean(expected_result):
            Check.error('Izraz {0} vrne {1!r} namesto {2!r}.',
                        expression, actual_result, expected_result)
            return False
        else:
            return True

    @staticmethod
    def run(statements, expected_state, clean=None, env=None, update_env=None):
        code = "\n".join(statements)
        statements = "  >>> " + "\n  >>> ".join(statements)
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get('clean', clean)
        exec(code, global_env)
        errors = []
        for (x, v) in expected_state.items():
            if x not in global_env:
                errors.append('morajo nastaviti spremenljivko {0}, vendar je ne'.format(x))
            elif clean(global_env[x]) != clean(v):
                errors.append('nastavijo {0} na {1!r} namesto na {2!r}'.format(x, global_env[x], v))
        if errors:
            Check.error('Ukazi\n{0}\n{1}.', statements,  ";\n".join(errors))
            return False
        else:
            return True

    @staticmethod
    @contextmanager
    def in_file(filename, content, encoding=None):
        encoding = Check.get('encoding', encoding)
        with open(filename, 'w', encoding=encoding) as f:
            for line in content:
                print(line, file=f)
        old_feedback = Check.current_part['feedback'][:]
        yield
        new_feedback = Check.current_part['feedback'][len(old_feedback):]
        Check.current_part['feedback'] = old_feedback
        if new_feedback:
            new_feedback = ['\n    '.join(error.split('\n')) for error in new_feedback]
            Check.error('Pri vhodni datoteki {0} z vsebino\n  {1}\nso se pojavile naslednje napake:\n- {2}', filename, '\n  '.join(content), '\n- '.join(new_feedback))

    @staticmethod
    @contextmanager
    def input(content, visible=None):
        old_stdin = sys.stdin
        old_feedback = Check.current_part['feedback'][:]
        try:
            with Check.set_stringio(visible):
                sys.stdin = Check.get('stringio')('\n'.join(content) + '\n')
                yield
        finally:
            sys.stdin = old_stdin
        new_feedback = Check.current_part['feedback'][len(old_feedback):]
        Check.current_part['feedback'] = old_feedback
        if new_feedback:
            new_feedback = ['\n  '.join(error.split('\n')) for error in new_feedback]
            Check.error('Pri vhodu\n  {0}\nso se pojavile naslednje napake:\n- {1}', '\n  '.join(content), '\n- '.join(new_feedback))

    @staticmethod
    def out_file(filename, content, encoding=None):
        encoding = Check.get('encoding', encoding)
        with open(filename, encoding=encoding) as f:
            out_lines = f.readlines()
        equal, diff, line_width = Check.difflines(out_lines, content)
        if equal:
            return True
        else:
            Check.error('Izhodna datoteka {0}\n  je enaka{1}  namesto:\n  {2}', filename, (line_width - 7) * ' ', '\n  '.join(diff))
            return False

    @staticmethod
    def output(expression, content, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        try:
            exec(expression, global_env)
        finally:
            output = sys.stdout.getvalue().strip().splitlines()
            sys.stdout = old_stdout
        equal, diff, line_width = Check.difflines(output, content)
        if equal:
            return True
        else:
            Check.error('Program izpiše{0}  namesto:\n  {1}', (line_width - 13) * ' ', '\n  '.join(diff))
            return False

    @staticmethod
    def difflines(actual_lines, expected_lines):
        actual_len, expected_len = len(actual_lines), len(expected_lines)
        if actual_len < expected_len:
            actual_lines += (expected_len - actual_len) * ['\n']
        else:
            expected_lines += (actual_len - expected_len) * ['\n']
        equal = True
        line_width = max(len(actual_line.rstrip()) for actual_line in actual_lines + ['Program izpiše'])
        diff = []
        for out, given in zip(actual_lines, expected_lines):
            out, given = out.rstrip(), given.rstrip()
            if out != given:
                equal = False
            diff.append('{0} {1} {2}'.format(out.ljust(line_width), '|' if out == given else '*', given))
        return equal, diff, line_width

    @staticmethod
    def init_environment(env=None, update_env=None):
        global_env = globals()
        if not Check.get('update_env', update_env):
            global_env = dict(global_env)
        global_env.update(Check.get('env', env))
        return global_env

    @staticmethod
    def generator(expression, expected_values, should_stop=None, further_iter=None, clean=None, env=None, update_env=None):
        from types import GeneratorType
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get('clean', clean)
        gen = eval(expression, global_env)
        if not isinstance(gen, GeneratorType):
            Check.error("Izraz {0} ni generator.", expression)
            return False

        try:
            for iteration, expected_value in enumerate(expected_values):
                actual_value = next(gen)
                if clean(actual_value) != clean(expected_value):
                    Check.error("Vrednost #{0}, ki jo vrne generator {1} je {2!r} namesto {3!r}.",
                                iteration, expression, actual_value, expected_value)
                    return False
            for _ in range(Check.get('further_iter', further_iter)):
                next(gen)  # we will not validate it
        except StopIteration:
            Check.error("Generator {0} se prehitro izteče.", expression)
            return False
        
        if Check.get('should_stop', should_stop):
            try:
                next(gen)
                Check.error("Generator {0} se ne izteče (dovolj zgodaj).", expression)
            except StopIteration:
                pass  # this is fine
        return True

    @staticmethod
    def summarize():
        for i, part in enumerate(Check.parts):
            if not Check.has_solution(part):
                print('{0}. podnaloga je brez rešitve.'.format(i + 1))
            elif not part['valid']:
                print('{0}. podnaloga nima veljavne rešitve.'.format(i + 1))
            else:
                print('{0}. podnaloga ima veljavno rešitev.'.format(i + 1))
            for message in part['feedback']:
                print('  - {0}'.format('\n    '.join(message.splitlines())))

    settings_stack = [{
        'clean': clean.__func__,
        'encoding': None,
        'env': {},
        'further_iter': 0,
        'should_stop': False,
        'stringio': VisibleStringIO,
        'update_env': False,
    }]

    @staticmethod
    def get(key, value=None):
        if value is None:
            return Check.settings_stack[-1][key]
        return value

    @staticmethod
    @contextmanager
    def set(**kwargs):
        settings = dict(Check.settings_stack[-1])
        settings.update(kwargs)
        Check.settings_stack.append(settings)
        try:
            yield
        finally:
            Check.settings_stack.pop()

    @staticmethod
    @contextmanager
    def set_clean(clean=None, **kwargs):
        clean = clean or Check.clean
        with Check.set(clean=(lambda x: clean(x, **kwargs))
                             if kwargs else clean):
            yield

    @staticmethod
    @contextmanager
    def set_environment(**kwargs):
        env = dict(Check.get('env'))
        env.update(kwargs)
        with Check.set(env=env):
            yield

    @staticmethod
    @contextmanager
    def set_stringio(stringio):
        if stringio is True:
            stringio = VisibleStringIO
        elif stringio is False:
            stringio = io.StringIO
        if stringio is None or stringio is Check.get('stringio'):
            yield
        else:
            with Check.set(stringio=stringio):
                yield


def _validate_current_file():
    def extract_parts(filename):
        with open(filename, encoding='utf-8') as f:
            source = f.read()
        part_regex = re.compile(
            r'# =+@(?P<part>\d+)=\s*\n' # beginning of header
            r'(\s*#( [^\n]*)?\n)+?'     # description
            r'\s*# =+\s*?\n'            # end of header
            r'(?P<solution>.*?)'        # solution
            r'(?=\n\s*# =+@)',          # beginning of next part
            flags=re.DOTALL | re.MULTILINE
        )
        parts = [{
            'part': int(match.group('part')),
            'solution': match.group('solution')
        } for match in part_regex.finditer(source)]
        # The last solution extends all the way to the validation code,
        # so we strip any trailing whitespace from it.
        parts[-1]['solution'] = parts[-1]['solution'].rstrip()
        return parts

    def backup(filename):
        backup_filename = None
        suffix = 1
        while not backup_filename or os.path.exists(backup_filename):
            backup_filename = '{0}.{1}'.format(filename, suffix)
            suffix += 1
        shutil.copy(filename, backup_filename)
        return backup_filename

    def submit_parts(parts, url, token):
        submitted_parts = []
        for part in parts:
            if Check.has_solution(part):
                submitted_part = {
                    'part': part['part'],
                    'solution': part['solution'],
                    'valid': part['valid'],
                    'secret': [x for (x, _) in part['secret']],
                    'feedback': json.dumps(part['feedback']),
                }
                if 'token' in part:
                    submitted_part['token'] = part['token']
                submitted_parts.append(submitted_part)
        data = json.dumps(submitted_parts).encode('utf-8')
        headers = {
            'Authorization': token,
            'content-type': 'application/json'
        }
        request = urllib.request.Request(url, data=data, headers=headers)
        response = urllib.request.urlopen(request)
        return json.loads(response.read().decode('utf-8'))

    def update_attempts(old_parts, response):
        updates = {}
        for part in response['attempts']:
            part['feedback'] = json.loads(part['feedback'])
            updates[part['part']] = part
        for part in old_parts:
            valid_before = part['valid']
            part.update(updates.get(part['part'], {}))
            valid_after = part['valid']
            if valid_before and not valid_after:
                wrong_index = response['wrong_indices'].get(str(part['part']))
                if wrong_index is not None:
                    hint = part['secret'][wrong_index][1]
                    if hint:
                        part['feedback'].append('Namig: {}'.format(hint))


    filename = os.path.abspath(sys.argv[0])
    file_parts = extract_parts(filename)
    Check.initialize(file_parts)

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxNzM4Mn0:1gOgYT:t9jeWVm9eyShbPI8CEgZrfbyKh8'
        try:
            odg = Check.current_part['solution']
            k1 = "'''"
            k2 = '"""'
            if k1 not in odg and k2 not in odg:
                Check.error("Kaj pa dokumentacijski komentar?")
            
            Check.equal("""prestej(5,[2, 5, 12, 3, 5, 3, 12, 8, 12])""", 2)
            Check.equal("""prestej(2,[2, 5, 12, 3, 5, 3, 12, 8, 12])""", 1)
            Check.equal("""prestej(12,[2, 5, 12, 3, 5, 3, 12, 8, 12])""", 3)
            Check.equal("""prestej(4,[2, 5, 12, 3, 5, 3, 12, 8, 12])""", 0)
            Check.equal("""prestej(2,[2, 2, 2, 2, 2, 2])""", 6)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxNzM4M30:1gOgYT:O2VgFAx9mixBdF7pWm0XRFpmyJY'
        try:
            if "'''" not in Check.current_part['solution'] and '"""' not in Check.current_part['solution']:
                Check.error("Kaj pa dokumentacijski komentar?")
            Check.equal("""prestejSode([2, 5, 12, 3, 5, 3, 12, 8, 12])""", 5) and \
                Check.equal("""prestejSode([2, 52, 12, 32, 52, 32, 12, 8, 12])""", 9) and \
                Check.equal("""prestejSode([21, 51, 121, 31, 51, 33, 127, 89, 125])""", 0) and \
                Check.equal("""prestejSode([])""", 0) and \
                Check.equal("""prestejSode([1])""", 0) and \
                Check.equal("""prestejSode([-13])""", 0) and \
                Check.equal("""prestejSode([-2, -2, 2, 2, 2, 2])""", 6) and \
                Check.equal("""prestejSode([-21, -22, -21, 21, 23, -1111211111])""", 1)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxNzM4NH0:1gOgYT:d7Bg8E3uMlloB7jGNmmxUPP6wyE'
        try:
            Check.equal("""prestejSodeLihe([2, 5, 12, 3, 5, 3, 12, 8, 12])""", (5, 4))
            Check.equal("""prestejSodeLihe([2, 52, 12, 32, 52, 32, 12, 8, 12])""", (9, 0))
            Check.equal("""prestejSodeLihe([21, 51, 121, 31, 51, 33, 127, 89, 125])""", (0, 9))
            Check.equal("""prestejSodeLihe([])""", (0, 0))
            Check.equal("""prestejSodeLihe([-2, -2, 2, 2, 2, 2])""", (6, 0))
            Check.equal("""prestejSodeLihe([-21, -22, -21, 21, 23, -1111211111])""", (1, 5))
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxNzM4NX0:1gOgYT:gu7Yzk5v6ZHY4erVaCBKdzwpXcY'
        try:
            Check.equal("""tabMest(5,[2, 5, 12, 3, 5, 3, 12, 8, 12])""", [1, 4])
            Check.equal("""tabMest(12,[2, 5, 12, 3, 5, 3, 12, 8, 12])""", [2, 6, 8])
            Check.equal("""tabMest(4,[2, 5, 12, 3, 5, 3, 12, 8, 12])""", [])
            Check.equal("""tabMest(4,[4, 4, 4, 4])""", [0, 1, 2, 3])
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxNzM4Nn0:1gOgYT:yTQFcd7BtD_LhQ7gjT6NsV_lEn4'
        try:
            Check.equal("""kolikoEnic([2, 5, 12, 1, 3, 5, 3, 12, 8, 12])""", [0, 1, 4, 2, 0, 2, 0, 0, 1, 0])
            Check.equal("""kolikoEnic([1432, 32155, 12, 351, 12353, 1255, 2313, 12, 8, 112])""", [0, 1, 4, 2, 0, 2, 0, 0, 1, 0])
            Check.equal("""kolikoEnic([])""", [0] * 10)
            Check.equal("""kolikoEnic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])""", [1] * 10)
            Check.equal("""kolikoEnic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])""", [2] * 10)
            Check.equal("""kolikoEnic([-1, -2, -3, 4, 5, -6, 7, 8, 9, -10, 1, 2, 3, -4, 5, 6, 7, 8, 9, 10])""", [2] * 10)
            Check.equal("""kolikoEnic([13132, 1315, 131234212, 24243, -5, -1, 3, -12, -8, 12])""", [0, 1, 4, 2, 0, 2, 0, 0, 1, 0])
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    print('Shranjujem rešitve na strežnik... ', end="")
    try:
        url = 'https://www.projekt-tomo.si/api/attempts/submit/'
        token = 'Token ac797f2c53c7c90311d269162e2f70771b1d5202'
        response = submit_parts(Check.parts, url, token)
    except urllib.error.URLError:
        print('PRI SHRANJEVANJU JE PRIŠLO DO NAPAKE! Poskusite znova.')
    else:
        print('Rešitve so shranjene.')
        update_attempts(Check.parts, response)
        if 'update' in response:
            print('Posodabljam datoteko... ', end="")
            backup_filename = backup(filename)
            with open(__file__, 'w', encoding='utf-8') as f:
                f.write(response['update'])
            print('Stara datoteka je bila preimenovana v {0}.'.format(backup_filename))
            print('Če se datoteka v urejevalniku ni osvežila, jo zaprite ter ponovno odprite.')
    Check.summarize()

if __name__ == '__main__':
    _validate_current_file()
