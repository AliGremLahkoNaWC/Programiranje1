# =============================================================================
# Zbiranje osebnih podatkov
#
# V "Uporaba slovarjev - razlaga" si lahko preberete, kako v Pythonu delamo s slovarji.
# 
# Tu pa rešite nekaj osnovnih nalog iz te teme.
# 
# V nekem podjetju zbirajo podatke o osebah, ki brskajo po medmrežju.
# Podatki so shranjeni v slovarjih (en slovar za vsako osebo). Ključ v
# takem slovarju je _lastnost_, vrednosti pa _podatek_ o tej lastnosti
# za določeno osebo. Primeri takšnih slovarjev:
# 
#     oseba1 = {'ime': 'Božidar', 'telefon': '031918211',
#               'obiskane spletne strani': ['facebook.com', 'google.com']}
#     oseba2 = {'naslov': 'Dunajska 105', 'številka noge': 42,
#               'prijatelji': ['Marko', 'Ana']}
# =====================================================================@020001=
# 1. podnaloga
# Sestavite funkcijo `podatek(oseba, lastnost)`, ki vrne podatek o
# lastnosti `lastnost`, ki jo imamo v slovarju `oseba`. Funkcija naj vrne
# `None`, če se ta podatek v slovarju ne nahaja. Primer:
# 
#     >>> podatek({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, 'naslov')
#     'Dunajska 105'
#     >>> podatek({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, 'prijatelji')
#     None
# 
# Pri tem ne smete uporabiti metode `get`!
# =============================================================================
def podatek(oseba,lastnost):
    ''' funkcija preveri ali slovar vsebuje neko lastnost in jo v primeru
    vsebovanosti, vrne'''
    if lastnost in oseba:
        return oseba[lastnost]
    return None
# =====================================================================@020002=
# 2. podnaloga
# Sestavite funkcijo `podatek_get(oseba, lastnost)`, ki vrne podatek o
# lastnosti `lastnost`, ki jo imamo v slovarju `oseba`. Funkcija naj vrne
# `None`, če se ta podatek v slovarju ne nahaja. Primer:
# 
#     >>> podatek_get({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, 'naslov')
#     'Dunajska 105'
#     >>> podatek_get({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, 'prijatelji')
#     None
# 
# Pri tem si nujno pomagajte z metodo `get`.
# =============================================================================
def podatek_get(oseba,lastnost):
    ''' funkcija preveri ali slovar vsebuje neko lastnost z
    metodo get in jo v primeru
    vsebovanosti, vrne'''
    if oseba.get(lastnost):
        return oseba[lastnost]
    return None
# =====================================================================@020003=
# 3. podnaloga
# Kadar oseba spremeni kak osebni podatek, moramo ta podatek v slovarju
# popraviti. Napišite funkcijo `popravi(oseba, lastnost, podatek)`, ki
# poleg slovarja `oseba`, sprejme `lastnost` in `podatek` o tej lastnosti ter
# podatek posodobi in vrne spremenjen slovar.
# Če lastnosti v slovarju ni, jo doda. Zgled:
# 
#     >>> popravi({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, 'naslov', 'Slovenska 5')
#     {'ime': 'Božidar', 'naslov': 'Slovenska 5'}
# 
#     >>> popravi({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, 'prijatelji', {'Nina', 'Vito'})
#     {'ime': 'Božidar', 'naslov': 'Dunajska 105', 'prijatelji': {'Nina', 'Vito'}}
# =============================================================================
def popravi(oseba,lastnost,podatek):

    oseba[lastnost] = podatek
    return oseba
# =====================================================================@020004=
# 4. podnaloga
# Oseba lahko spremeni tudi več osebnih podatkov naenkrat. Takrat moramo
# popraviti vse spremenjene podatke v slovarju.
# Napišite funkcijo `popravi_vec(oseba, novi)`, ki poleg slovarja `oseba`,
# sprejme slovar `novi`, v katerem so vse lastnosti in pripadajoči podatki,
# ki jih po moramo popraviti in vrne
# spremenjen slovar. Če kakšnih lastnosti v slovarju ni, jih doda. Zgled:
# 
#     >>> popravi_vec({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, {'naslov': 'Slovenska 5', 'prijatelji': {'Nina', 'Vito'}})
#     {'ime': 'Božidar', 'naslov': 'Slovenska 5', 'prijatelji': {'Nina', 'Vito'}}
# 
# Namig: pomagate si lahko z metodo `update`.
# =============================================================================
def popravi_vec(oseba,novi):

    oseba.update(novi)
    for key in novi:
        if key in oseba:
            oseba[key] = novi[key]
        

    return oseba
# =====================================================================@020005=
# 5. podnaloga
# Včasih kaka lastnost o določeni osebi ne drži več. Takrat jo moramo iz slovarja
# neumudoma izbrisati, čeprav nimamo njene nove vrednosti.
# Napišite funkcijo `izbrisi(oseba, lastnost)`, ki poleg slovarja `oseba`,
# sprejme lastnost `lastnost` ter jo iz slovarja izbriše in vrne spremenjen slovar.
# Če lastnosti v slovarju ni, samo vrne vhodni slovar. Zgled:
# 
#     >>> izbrisi({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, 'naslov')
#     {'ime': 'Božidar'}
# 
#     >>> izbrisi({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, 'prijatelji')
#     {'ime': 'Božidar', 'naslov': 'Dunajska 105'}
# =============================================================================
def izbrisi(oseba,lastnost):

    if lastnost in oseba:
        del oseba[lastnost]
        
    return oseba
# =====================================================================@020006=
# 6. podnaloga
# Napišite funkcijo `ista_oseba(oseba1, oseba2)`, ki pove, ali slovarja
# `oseba1` in `oseba2` predstavljata isto osebo. Isto oseba predstavljata
# takrat, kadar vsebujeta iste lastnosti z istimi vrednostmi. Zgled:
# 
#     >>> ista_oseba({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, {'ime': 'Sara', 'naslov': 'Dunajska 105'})
#     False
# 
#     >>> ista_oseba({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, {'naslov': 'Dunajska 105', 'ime': 'Božidar',})
#     True
# 
# Namig: lahko si pomagate z operatorjem `==`.
# =============================================================================
def ista_oseba(oseba1,oseba2):
    
    if oseba1 == oseba2:
        return True
    elif oseba1 == {} or oseba2 == {}:
        return False
    for key, val in oseba1.items():
        if key in oseba2 and oseba2[key] == val:
            pass
        else:
            return False
    return True
# =====================================================================@020007=
# 7. podnaloga
# Za osebi `oseba1` in `oseba2` pravimo, da se _ujemata_ v lastnosti
# `lastnost`, če za obe osebi poznamo podatka o tej lastnosti in sta
# podatka enaka. Če pa za obe osebi poznamo podatka in sta podatka
# različna, pa pravimo, da se osebi _razlikujeta_ v lastnosti `lastnost`.
# Na primer, osebi
# 
#     oseba1 = {'ime': 'Janez', 'priimek': 'Novak'}
#     oseba2 = {'ime': 'Jože', 'priimek': 'Novak', 'starost': 20}
# 
# se ujemata v lastnosti `'priimek'` in razlikujeta v lastnosti `'ime'`.
# (V lastnosti `'starost'` se niti ne ujemata niti ne razlikujeta.)
# 
# Sestavite funkcijo `ujemanje(oseba1, oseba2)`, ki pove, v koliko
# lastnostih se osebi `oseba1` in `oseba2` ujemata in v koliko lastnostih
# se razlikujeta. Rezultat naj funkcija vrne kot tabelo z dvema elementoma.
# Primer:
# 
#     >>> ujemanje({'ime': 'Janez', 'priimek': 'Novak'},
#                  {'ime': 'Jože', 'priimek': 'Novak', 'starost': 20})
#     [1, 1]
# 
# Namig: uporabite zanko `for`.
# =============================================================================
def ujemanje(oseba1, oseba2):

    tab_razlik = [0,0]

    if len(oseba1) > len(oseba2):

        for key, val in oseba1.items():
            if key in oseba2 and oseba2[key] == val:
                tab_razlik[0] = tab_razlik[0] + 1
            if key in oseba2 and oseba2[key] != val:
                tab_razlik[1] = tab_razlik[1] + 1
    elif len(oseba2) > len(oseba1):
        for key, val in oseba2.items():
            if key in oseba1 and oseba1[key] == val:
                tab_razlik[0] = tab_razlik[0] + 1
            if key in oseba1 and oseba1[key] != val:
                tab_razlik[1] = tab_razlik[1] + 1
    else:
        for key, val in oseba1.items():
            if key in oseba2 and oseba2[key] == val:
                tab_razlik[0] = tab_razlik[0] + 1
            if key in oseba2 and oseba2[key] != val:
                tab_razlik[1] = tab_razlik[1] + 1


            

           
    return tab_razlik




































































































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
        Check.current_part['token'] = 'eyJwYXJ0IjoyMDAwMSwidXNlciI6MzM2N30:1gzH8K:KUu-W5yMSL6O70zKMyU4V-FJX4w'
        try:
            if '.get' in Check.current_part['solution']:
                Cheeck.error('Uporaba metode get ni dovoljena!')
                
            test_data = [
                ({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, 'naslov', 'Dunajska 105'),
                ({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, 'prijatelji', None),
                ({'ime': 'Anja', 'barva oči': 'zelena', 'obsegi': [82, 58, 82], 'IP': '193.77.34.1'}, 'IP', '193.77.34.1'),
            ]
            for oseba, lastnost, vrednost in test_data:
                if not Check.equal("podatek({0}, '{1}')".format(oseba, lastnost), vrednost):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoyMDAwMiwidXNlciI6MzM2N30:1gzH8K:xJp-39hfCwA3EogqDPJx8XiC97w'
        try:
            if '.get' not in Check.current_part['solution']:
                Cheeck.error('Obvezna je uporaba metode get!')
                             
            test_data = [
                ({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, 'naslov', 'Dunajska 105'),
                ({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, 'prijatelji', None),
                ({'ime': 'Anja', 'barva oči': 'zelena', 'obsegi': [82, 58, 82], 'IP': '193.77.34.1'}, 'IP', '193.77.34.1'),
            ]
            for oseba, lastnost, vrednost in test_data:
                if not Check.equal("podatek_get({0}, '{1}')".format(oseba, lastnost), vrednost):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoyMDAwMywidXNlciI6MzM2N30:1gzH8K:pBsgRpPeUnYno-q0cgz5JHogyBQ'
        try:
            Check.equal("popravi({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, 'naslov', 'Slovenska 5')",
                        {'ime': 'Božidar', 'naslov': 'Slovenska 5'}) and \
            Check.equal("popravi({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, 'prijatelji', {'Nina', 'Vito'})",
                        {'ime': 'Božidar', 'naslov': 'Dunajska 105', 'prijatelji': {'Nina', 'Vito'}}) and \
            Check.equal("popravi({'ime': 'Sara', 'naslov': 'Dunajska 105'}, 'šola', 'fmf')",
                        {'ime': 'Sara', 'naslov': 'Dunajska 105', 'šola': 'fmf'}) and \
            Check.equal("popravi({}, 'šola', 'fmf')",
                        {'šola': 'fmf'})
            
            Check.secret(popravi({'ime': 'Sara'}, 'šola', 'fmf'))
            Check.secret(popravi({'ime': 'Sara'}, 'ime', 'Sanja'))
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoyMDAwNCwidXNlciI6MzM2N30:1gzH8K:1NqjbLv1uDB6RGWpWBG8X0SrY2A'
        try:
            Check.equal("popravi_vec({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, {'naslov': 'Slovenska 5', 'prijatelji': {'Nina', 'Vito'}})",
                        {'ime': 'Božidar', 'naslov': 'Slovenska 5', 'prijatelji': {'Nina', 'Vito'}}) and \
            Check.equal("popravi_vec({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, {'naslov': 'Slovenska 5'})",
                        {'ime': 'Božidar', 'naslov': 'Slovenska 5'}) and \
            Check.equal("popravi_vec({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, {'prijatelji': {'Nina', 'Vito'}, 'naslov': 'Slovenska 5'})",
                        {'ime': 'Božidar', 'naslov': 'Slovenska 5', 'prijatelji': {'Nina', 'Vito'}}) and \
            Check.equal("popravi_vec({'ime': 'Sara', 'naslov': 'Dunajska 105'}, {})",
                        {'ime': 'Sara', 'naslov': 'Dunajska 105'}) and \
            Check.equal("popravi_vec({}, {'šola': 'fmf'})",
                        {'šola': 'fmf'}) and \
            Check.equal("popravi_vec({}, {})", {})
            
            
            Check.secret(popravi_vec({'ime': 'Sanja', 'naslov': 'Dunajska 105'}, {'ime': 'Nina', 'prijatelji': {'Eva'}}))
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoyMDAwNSwidXNlciI6MzM2N30:1gzH8K:qcKqkiiVm5PnA5trjRFXPRrX3cU'
        try:
            Check.equal("izbrisi({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, 'naslov')",
                        {'ime': 'Božidar'}) and \
            Check.equal("izbrisi({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, 'prijatelji')",
                        {'ime': 'Božidar', 'naslov': 'Dunajska 105'}) and \
            Check.equal("izbrisi({'ime': 'Sara', 'naslov': 'Dunajska 105'}, 'ime')",
                        {'naslov': 'Dunajska 105'}) and \
            Check.equal("izbrisi({}, 'ime')",
                        {})
            
            
            Check.equal("izbrisi({'ime': 'Sara', 'naslov': 'Slovenska 5'}, 'poročena')", {'ime': 'Sara', 'naslov': 'Slovenska 5'})
            Check.equal("izbrisi({'ime': 'Sara', 'poročena': False}, 'poročena')", {'ime': 'Sara'})
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoyMDAwNiwidXNlciI6MzM2N30:1gzH8K:iTpLaubS1UT4orqSxihHKEH0ROA'
        try:
            Check.equal("ista_oseba({'ime': 'Božidar', 'naslov': 'Dunajska 105'},"
                        "{'ime': 'Sara', 'naslov': 'Dunajska 105'})", False) and \
            Check.equal("ista_oseba({'ime': 'Božidar', 'naslov': 'Dunajska 105'},"
                        "{'naslov': 'Dunajska 105', 'ime': 'Božidar',})", True) and \
            Check.equal("ista_oseba({}, {})", True) and \
            Check.equal("ista_oseba({}, {'ime': 'Božidar', 'naslov': 'Dunajska 105'})", False)
            
            Check.secret(ista_oseba({'priimek': 'Novak'}, {'ime': 'Janez'}))
            Check.secret(ista_oseba({'priimek': 'Novak'}, {'priimek': 'Janez'}))
            Check.secret(ista_oseba({'priimek': 'Novak'}, {'priimek': 'Novak'}))
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoyMDAwNywidXNlciI6MzM2N30:1gzH8K:UYb5I0b8mf2fA1NXs5cbZw26Sfc'
        try:
            test_data = [
                ({'ime': 'Janez', 'priimek': 'Novak'},
                 {'ime': 'Jože', 'priimek': 'Novak', 'starost': 20},
                 [1, 1]),
                ({'ime': 'Božidar', 'telefon': '031918211', 'obiskane spletne strani': ['facebook.com', 'google.com']},
                 {'naslov': 'Dunajska 105', 'številka noge': 42, 'obiskane spletne strani': ['facebook.com', 'google.com']},
                 [1, 0]),
            ]
            for oseba1, oseba2, vrednost in test_data:
                if not Check.equal("ujemanje({0}, {1})".format(oseba1, oseba2), vrednost):
                    break
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
