# =============================================================================
# Slovensko-angleški slovarček
#
# Slovár ali besednják  je po [Wikipediji](https://www.wikiwand.com/sl/Slovar)
# knjiga, v katerem so abecedno urejene in pojasnjene besede nekega jezika.
# 
# Slovar lahko v Pythonu predstavimo s slovarjem – presenetljivo, kajne?
# Natančneje, ključi v slovarju so besede, pripadajoče vrednosti pa so
# množice vseh možnih prevodov. Na primer:
# 
#     {'je': {'is', 'eats'}, 'kosilo': {'lunch'},
#      'mama': {'mother', 'mum', 'mummy'}}
# =====================================================================@019573=
# 1. podnaloga
# Sestavite funkcijo `obratni(slov)`, ki vrne obratni slovar danega
# slovarja `slov`.
# 
#     >>> obratni({'je': {'is', 'eats'}, 'žre': {'bugs', 'eats'}})
#     {'bugs': {'žre'}, 'eats': {'je', 'žre'}, 'is': {'je'}}
# =============================================================================
def obratni(slov):
    '''funkcija vrne obratni slovar od podanega'''
    slovar = dict()

    for key, val in slov.items():
        for beseda in val:
            if beseda not in slovar:
                slovar[beseda] = set()
                slovar[beseda].add(key)
            else:
                slovar[beseda].add(key)
    return slovar
# =====================================================================@019574=
# 2. podnaloga
# Sestavite funkcijo `nedvoumne_in_dvoumne(slov)`, ki vrne par dveh množic:
# v prvi naj bodo vse besede iz slovarja `slov`, ki imajo natanko en možen
# prevod, v drugi pa vse tiste, ki jih imajo več.
# 
#     >>> nedvoumne_in_dvoumne({'je': {'is', 'eats'}, 'kosilo': {'lunch'}, 'solata': {'salad'}}
#     ({'kosilo', 'solata'}, {'je'})
# =============================================================================
def nedvoumne_in_dvoumne(slov):
    '''funkcija vrne par dveh množic, kjer so vse ebsede iz slovarja slov
    z enim samim prevodom, ter v drugi množici besede, ki imajo več prevodov'''

    mn1, mn2 = set(), set()
    for key, val in slov.items():
        if len(val) > 1:
            mn2.add(key)
        else:
            mn1.add(key)

    return mn1,mn2
# =====================================================================@019575=
# 3. podnaloga
# Sestavite funkcijo `vsi_mozni_prevodi(slov, stav)`, ki vrne množico
# vseh možnih “prevodov” danega stavka `stav` glede na dani slovar `slov`.
# Stavek je niz, sestavljen iz besed, ločenih s presledki. Če besede ni v
# slovarju, naj v prevodu ostane taka, kakršna je.
# 
# _Namig:_ sestavite še pomožno funkcijo, ki namesto niza `stav` sprejme
# seznam besed.
# =============================================================================
def vsi_mozni_prevodi(slov, stav):
    '''vrne mnozico vseh moznih prevodov danega stavka, glede na dani slovar'''

    mn = set()
    pom_slovar = dict()
    stavek = stav.split()
    return None
# =====================================================================@019576=
# 4. podnaloga
# Sestavite funkcijo `preberi(vhod)`, ki prebere datoteko z imenom `vhod`
# in vrne slovar, zapisan v njej. Slovar je v datoteki predstavljen tako,
# da je vsaka beseda v svoji vrstici, pod njo pa so v vrsticah, ki se
# začnejo z znakom `-`, zapisani njeni prevodi. Na primer, v datoteki
# 
#     je
#     - is
#     - eats
#     kosilo
#     - lunch
#     mama
#     - mother
#     - mum
#     - mummy
# 
# je zapisan ravno slovar
# 
#     {'je': {'is', 'eats'}, 'kosilo': {'lunch'},
#      'mama': {'mother', 'mum', 'mummy'}}
# 
# Predpostavite lahko, da je vhodna datoteka vedno zgornje oblike.
# =============================================================================
def preberi(vhod):
    '''funkcija sestavi slovar iz dane datoteke'''
    slovar = dict()
    key = ''
    for vrstica in open(vhod, 'r'):
        if '-' not in vrstica:
            key = vrstica.strip()
            slovar[key] = set()
        else:
            vrstica = vrstica.strip().split()
            slovar[key].add(vrstica[1])
    return slovar


































































































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
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxOTU3M30:1hOcgj:VelRtftRhQJQXHIa-nB8lR8Est8'
        try:
            tests = [
                    ("obratni({'je': {'is', 'eats'}, 'žre': {'bugs', 'eats'}})",\
                        {'bugs': {'žre'}, 'eats': {'je', 'žre'}, 'is': {'je'}}),
                    ("obratni({'je': {'is', 'eats'}, 'kosilo': {'lunch'}, 'mama': {'mother', 'mum', 'mummy'}})",\
                        {'mother': {'mama'}, 'mum': {'mama'}, 'eats': {'je'}, 'lunch': {'kosilo'}, 'mummy': {'mama'}, 'is': {'je'}}),
                    ("obratni({'mother': {'mama'}, 'mum': {'mama'}, 'eats': {'je'}, 'lunch': {'kosilo'}, 'mummy': {'mama'}, 'is': {'je'}})",\
                        {'je': {'is', 'eats'}, 'kosilo': {'lunch'}, 'mama': {'mother', 'mum', 'mummy'}})
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxOTU3NH0:1hOcgj:5_SdW6Azg5Pjz6Z-zeyUcXsroiI'
        try:
            tests = [
                    ("nedvoumne_in_dvoumne({'je': {'is', 'eats'}, 'kosilo': {'lunch'}, 'solata': {'salad'}})", ({'kosilo', 'solata'}, {'je'})),
                    ("nedvoumne_in_dvoumne({'je': {'is', 'eats'}, 'kosilo': {'lunch'}, 'mama': {'mother', 'mum', 'mummy'}})", ({'kosilo'}, {'je', 'mama'}))
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxOTU3NX0:1hOcgj:nknR3mBUFRaDdfi67qyhKnJwZQE'
        try:
            tests = [
                        ("vsi_mozni_prevodi({'je': {'is', 'eats'}, 'kosilo': {'lunch'}, 'mama': {'mother', 'mum', 'mummy'}}, 'mama je kosilo')",
                        {'mummy eats lunch', 'mother is lunch', 'mummy is lunch', 'mum eats lunch', 'mother eats lunch', 'mum is lunch'}) ,
            
                        ("vsi_mozni_prevodi({'je': {'is', 'eats'}, 'kosilo': {'lunch'}, 'mama': {'mother', 'mum', 'mummy'}}, 'Franci je kosilo')",
                        {'Franci eats lunch', 'Franci is lunch'}) ,
            
                        ("vsi_mozni_prevodi({'je': {'is', 'eats'}, 'kosilo': {'lunch'}, 'mama': {'mother', 'mum', 'mummy'}}, 'Franci in mama jesta kosilo')",
                        {'Franci in mother jesta lunch', 'Franci in mum jesta lunch', 'Franci in mummy jesta lunch'}) ,
            
                        ("vsi_mozni_prevodi({'je': {'is', 'eats'}, 'kosilo': {'lunch'}, 'mama': {'mother', 'mum', 'mummy'}}, 'Tudi danes mama je kosilo')",
                        {'Tudi danes mummy eats lunch', 'Tudi danes mother is lunch', 'Tudi danes mummy is lunch', 'Tudi danes mum eats lunch',
                         'Tudi danes mother eats lunch', 'Tudi danes mum is lunch'}) ,
            
                        ("vsi_mozni_prevodi({'danes' : {'today'}, 'je': {'is', 'eats'}, 'kosilo': {'lunch'}, 'mama': {'mother', 'mum', 'mummy'}}, 'Tudi danes mama je kosilo')",
                        {'Tudi today mummy eats lunch', 'Tudi today mother is lunch', 'Tudi today mummy is lunch',
                         'Tudi today mum eats lunch', 'Tudi today mother eats lunch', 'Tudi today mum is lunch'}) ,
            
                        ("""vsi_mozni_prevodi({'par' : {'couple', 'pair', 'two'}, 'danes' : {'today'}, 'je': {'is', 'eats'}, 'kosilo': {'lunch'}, 
                        'mama': {'mother', 'mum', 'mummy'}}, 'Tudi danes mama in par je kosilo')""",
                        {'Tudi today mummy in pair eats lunch', 'Tudi today mother in pair is lunch', 'Tudi today mummy in pair is lunch',
                         'Tudi today mum in pair eats lunch', 'Tudi today mother in pair eats lunch', 'Tudi today mum in pair is lunch',
                         'Tudi today mummy in couple eats lunch', 'Tudi today mother in couple is lunch', 'Tudi today mummy in couple is lunch',
                         'Tudi today mum in couple eats lunch', 'Tudi today mother in couple eats lunch', 'Tudi today mum in couple is lunch',
                         'Tudi today mummy in two eats lunch', 'Tudi today mother in two is lunch', 'Tudi today mummy in two is lunch',
                         'Tudi today mum in two eats lunch', 'Tudi today mother in two eats lunch', 'Tudi today mum in two is lunch'}) ,
            
                        ("""vsi_mozni_prevodi({'par' : {'couple', 'pair', 'two'}, 'danes' : {'today'}, 'je': {'is', 'eats'}, 'kosilo': {'lunch'}, 
                        'mama': {'mother', 'mum', 'mummy'}, 'in' : {'and'}}, 'Tudi danes mama in par je kosilo')""",
                        {'Tudi today mummy and pair eats lunch', 'Tudi today mother and pair is lunch', 'Tudi today mummy and pair is lunch',
                         'Tudi today mum and pair eats lunch', 'Tudi today mother and pair eats lunch', 'Tudi today mum and pair is lunch',
                         'Tudi today mummy and couple eats lunch', 'Tudi today mother and couple is lunch', 'Tudi today mummy and couple is lunch',
                         'Tudi today mum and couple eats lunch', 'Tudi today mother and couple eats lunch', 'Tudi today mum and couple is lunch',
                         'Tudi today mummy and two eats lunch', 'Tudi today mother and two is lunch', 'Tudi today mummy and two is lunch',
                         'Tudi today mum and two eats lunch', 'Tudi today mother and two eats lunch', 'Tudi today mum and two is lunch'}) ,
            
                        ("""vsi_mozni_prevodi({'a' : {'X', 'Y', 'Z'}, 'b' : {'1', '2', '3', '4'}}, 'a b')""",
                        {'X 1', 'X 2', 'X 3', 'X 4', 'Y 1', 'Y 2', 'Y 3', 'Y 4', 'Z 1', 'Z 2', 'Z 3', 'Z 4'}) ,
            
                        ("""vsi_mozni_prevodi({'a' : {'X', 'Y', 'Z'}, 'b' : {'1', '2', '3', '4'}}, 'aa a b')""",
                        {'aa X 1', 'aa X 2', 'aa X 3', 'aa X 4', 'aa Y 1', 'aa Y 2', 'aa Y 3', 'aa Y 4', 'aa Z 1', 'aa Z 2', 'aa Z 3', 'aa Z 4'}) ,
            ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxOTU3Nn0:1hOcgj:ZUVV2bc22BdBGAxFyw7NhUxjUUc'
        try:
            with Check.in_file('slovar_1.txt', ['je',
                                               '- is',
                                               '- eats',
                                               'kosilo',
                                               '- lunch',
                                               'mama',
                                               '- mother',
                                               '- mum',
                                               '- mummy']):
                Check.equal("preberi('slovar_1.txt')", {'je': {'is', 'eats'}, 'kosilo': {'lunch'}, 'mama': {'mother', 'mum', 'mummy'}})
            with Check.in_file('slovar_2.txt', ['je',
                                               '- is',
                                               '- eats',
                                               'žre',
                                               '- bugs',
                                               '- eats']):
                Check.equal("preberi('slovar_2.txt')", {'je': {'is', 'eats'}, 'žre': {'bugs', 'eats'}})
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
