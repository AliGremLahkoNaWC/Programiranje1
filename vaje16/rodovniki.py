# =============================================================================
# Rodovniki
#
# Ukvarjali se bomo z rodovniki (Celjskih grofov in drugih).
# Rodovnik imamo podan kot slovar, kjer je ključ ime "glave rodbine"
# vrednost pa tabela imen otrok. Recimo:
# 
#     rodovnik =
#      {'Ulrik I.': ['Viljem'], 'Margareta': [], 'Herman I.': ['Herman II.', 'Hans'],
#       'Elizabeta II.': [], 'Viljem': ['Ana Poljska'], 'Elizabeta I.': [],
#       'Ana Poljska': [], 'Herman III.': ['Margareta'], 'Ana Ortenburška': [],
#       'Barbara': [], 'Herman IV.': [], 'Katarina': [], 'Friderik III.': [],
#       'Herman II.': ['Ludvik', 'Friderik II.', 'Herman III.', 'Elizabeta I.', 'Barbara'],
#       'Ulrik II.': ['Herman IV.', 'Jurij', 'Elizabeta II.'], 'Hans': [], 'Ludvik': [],
#       'Friderik I.': ['Ulrik I.', 'Katarina', 'Herman I.', 'Ana Ortenburška'],
#       'Friderik II.': ['Friderik III.', 'Ulrik II.'], 'Jurij': []}
#      rodovnik['Friderik II.']
# 
# nam torej vrne
# 
#       ['Friderik III.', 'Ulrik II.']
# =====================================================================@020194=
# 1. podnaloga
# Število otrok
# 
# Sestavi funkcijo `koliko_otrok(ime, rodovnik)`, ki za dano ime in
# rodovnik vrne število otrok te osebe, oz None, če osebe ni v rodovniku.
# =============================================================================
def koliko_otrok(ime,rodovnik):
    '''funkcija preveri koliko otrok pripada dani osebi, po rodovniku'''
    otroci = 0
    if ime in rodovnik:
        otroci = len(rodovnik[ime])
        return otroci
    return None
    
# =====================================================================@020195=
# 2. podnaloga
# Število potomcev
# 
# Sestavi funkcijo `koliko_potomcev(ime, rodovnik)`, ki za dano `ime` in
# `rodovnik` vrne število potomcev te osebe. Če osebe ni v rodovniku, vrni None
# =============================================================================
def koliko_potomcev(ime,rodovnik):
    '''funkcija šteje generacije potomcev za dano osebo'''
    potomci = koliko_otrok(ime,rodovnik)
    if potomci == None:
        return None
    for oseba in rodovnik[ime]:
        potomci = potomci + koliko_potomcev(oseba,rodovnik)
    return potomci
# =====================================================================@020196=
# 3. podnaloga
# Je v rodbini?
# 
# Sestavi funkcijo `je_v_rodbini(ime, glava_rodbine, rodovnik)`, ki ugotovi, ali
# je oseba z imenom `ime` v rodbini osebe `glava_rodbine`.
# =============================================================================
def je_v_rodbini(ime,glava_rodbine,rodovnik):
    '''funkcija poizve ali je podana oseba v rodbini'''
    
    
    
# =====================================================================@020197=
# 4. podnaloga
# Kdo se podpisuje najdlje časa?
# 
# Sestavi funkcijo `najdaljsi_podpis(glava_rodbine, rodovnik)`, ki ugotovi, kdo
# v rodbini osebe `glava_rodbine` ima najdaljše ime za podpis (torej kompletno
# ime).
# =============================================================================

# =====================================================================@020198=
# 5. podnaloga
# Kdo ima najkrajše ime?
# 
# Sestavi funkcijo `najkrajse_ime(glava_rodbine, rodovnik)`, ki ugotovi, kdo
# v rodbini osebe `glava_rodbine` ima najkrajše ime.
# (šteje samo krstno ime, brez "Ortenburga" in "Celja" ter brez številk)?
# =============================================================================

# =====================================================================@020199=
# 6. podnaloga
# Globina rodbine
# 
# "Globino" rodbine definiramo tako: če nekdo nima otrok, je globina njegove
# rodbine 1. Če ima otroka, ta pa nima vnukov (ali celo več otrok, ti pa
# nimajo vnukov), je globina rodbine 2. Če nekdo ima vnuke, vendar nobenega
# pravnuka, je globina njegove rodbine 3.
# 
# Sestavi funkcijo `globina(glava_rodbine, rodovnik)`, ki vrne globino rodbine
# osebe `glava_rodbine` v rodovniku `rodovnik`
# =============================================================================





































































































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
        Check.current_part['token'] = 'eyJwYXJ0IjoyMDE5NCwidXNlciI6MzM2N30:1h4LN5:8LIesnz3RgsgFMt4eKwLUeqntD0'
        try:
            rodovnikCG = {
             'Ulrik I.': ['Viljem'], 'Margareta': [], 'Herman I.': ['Herman II.', 'Hans'],
             'Elizabeta II.': [], 'Viljem': ['Ana Celjska'], 'Elizabeta I.': [],
             'Ana Celjska': [], 'Herman III.': ['Margareta'], 'Ana Ortenburška': [],
             'Barbara': [], 'Herman IV.': [], 'Katarina': [], 'Friderik III.': [],
             'Herman II.': ['Ludvik', 'Friderik II.', 'Herman III.', 'Elizabeta I.', 'Barbara'],
             'Ulrik II.': ['Herman IV.', 'Jurij', 'Elizabeta II.'], 'Hans': [], 'Ludvik': [],
             'Friderik I.': ['Ulrik I.', 'Katarina', 'Herman I.', 'Ana Ortenburška'],
             'Friderik II.': ['Friderik III.', 'Ulrik II.'], 'Jurij': []}
            
            tests = [
                    ("koliko_otrok('Friderik I.', rodovnikCG)", 4, {'rodovnikCG': rodovnikCG}),
                    ("koliko_otrok('Matija I.', rodovnikCG)", None, {'rodovnikCG': rodovnikCG}),
                    ("koliko_otrok('Friderik II.', rodovnikCG)", 2, {'rodovnikCG': rodovnikCG}),
                    ("koliko_otrok('Ulrik I.', rodovnikCG)", 1, {'rodovnikCG': rodovnikCG}),
                    ("koliko_otrok('Hans', rodovnikCG)", 0, {'rodovnikCG': rodovnikCG}),
                    ("koliko_otrok('Herman II.', rodovnikCG)", 5, {'rodovnikCG': rodovnikCG})
                    ]
            
            for expression, result, env in tests:
                if not Check.equal(expression, result, env=env):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoyMDE5NSwidXNlciI6MzM2N30:1h4LN5:OVN8fhCEBcuyjiW10t5zSOhzBPY'
        try:
            rodovnikCG = {
             'Ulrik I.': ['Viljem'], 'Margareta': [], 'Herman I.': ['Herman II.', 'Hans'],
             'Elizabeta II.': [], 'Viljem': ['Ana Celjska'], 'Elizabeta I.': [],
             'Ana Celjska': [], 'Herman III.': ['Margareta'], 'Ana Ortenburška': [],
             'Barbara': [], 'Herman IV.': [], 'Katarina': [], 'Friderik III.': [],
             'Herman II.': ['Ludvik', 'Friderik II.', 'Herman III.', 'Elizabeta I.', 'Barbara'],
             'Ulrik II.': ['Herman IV.', 'Jurij', 'Elizabeta II.'], 'Hans': [], 'Ludvik': [],
             'Friderik I.': ['Ulrik I.', 'Katarina', 'Herman I.', 'Ana Ortenburška'],
             'Friderik II.': ['Friderik III.', 'Ulrik II.'], 'Jurij': []}
            
            tests = [
                    ("koliko_potomcev('Friderik I.', rodovnikCG)", 19, {'rodovnikCG': rodovnikCG}),
                    ("koliko_potomcev('Friderik II.', rodovnikCG)", 5, {'rodovnikCG': rodovnikCG}),
                    ("koliko_potomcev('Matija I.', rodovnikCG)", None, {'rodovnikCG': rodovnikCG}),
                    ("koliko_potomcev('Ulrik I.', rodovnikCG)", 2, {'rodovnikCG': rodovnikCG}),
                    ("koliko_potomcev('Hans', rodovnikCG)", 0, {'rodovnikCG': rodovnikCG}),
                    ("koliko_potomcev('Herman II.', rodovnikCG)", 11, {'rodovnikCG': rodovnikCG})
                    ]
            
            for expression, result, env in tests:
                if not Check.equal(expression, result, env=env):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoyMDE5NiwidXNlciI6MzM2N30:1h4LN5:hzCL5CBWObueTwe2kw0XYxNtk6k'
        try:
            rodovnikCG = {
             'Ulrik I.': ['Viljem'], 'Margareta': [], 'Herman I.': ['Herman II.', 'Hans'],
             'Elizabeta II.': [], 'Viljem': ['Ana Celjska'], 'Elizabeta I.': [],
             'Ana Celjska': [], 'Herman III.': ['Margareta'], 'Ana Ortenburška': [],
             'Barbara': [], 'Herman IV.': [], 'Katarina': [], 'Friderik III.': [],
             'Herman II.': ['Ludvik', 'Friderik II.', 'Herman III.', 'Elizabeta I.', 'Barbara'],
             'Ulrik II.': ['Herman IV.', 'Jurij', 'Elizabeta II.'], 'Hans': [], 'Ludvik': [],
             'Friderik I.': ['Ulrik I.', 'Katarina', 'Herman I.', 'Ana Ortenburška'],
             'Friderik II.': ['Friderik III.', 'Ulrik II.'], 'Jurij': []}
            
            tests = [
                    ("je_v_rodbini('Friderik I.', 'Friderik I.', rodovnikCG)", True, {'rodovnikCG': rodovnikCG}),
                    ("je_v_rodbini('Friderik II.', 'Friderik I.', rodovnikCG)", True, {'rodovnikCG': rodovnikCG}),
                    ("je_v_rodbini('Friderik I.', 'Friderik II.', rodovnikCG)", False, {'rodovnikCG': rodovnikCG}),
                    ("je_v_rodbini('Jurij', 'Herman II.', rodovnikCG)", True, {'rodovnikCG': rodovnikCG}),
                    ("je_v_rodbini('Hans', 'Katarina', rodovnikCG)", False, {'rodovnikCG': rodovnikCG}),
                    ("je_v_rodbini('Ludvik', 'Herman II.', rodovnikCG)", True, {'rodovnikCG': rodovnikCG}),
                    ("je_v_rodbini('Ludvik', 'Ulrik I.', rodovnikCG)", False, {'rodovnikCG': rodovnikCG})
                    ]
            
            for expression, result, env in tests:
                if not Check.equal(expression, result, env=env):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoyMDE5NywidXNlciI6MzM2N30:1h4LN5:WSPtPNFennpNCLrJmQrkBNLDiZU'
        try:
            rodovnikCG = {
             'Ulrik I.': ['Viljem'], 'Margareta': [], 'Herman I.': ['Herman II.', 'Hans'],
             'Elizabeta II.': [], 'Viljem': ['Ana Celjska'], 'Elizabeta I.': [],
             'Ana Celjska': [], 'Herman III.': ['Margareta'], 'Ana Ortenburška': [],
             'Barbara': [], 'Herman IV.': [], 'Katarina': [], 'Friderik III.': [],
             'Herman II.': ['Ludvik', 'Friderik II.', 'Herman III.', 'Elizabeta I.', 'Barbara'],
             'Ulrik II.': ['Herman IV.', 'Jurij', 'Elizabeta II.'], 'Hans': [], 'Ludvik': [],
             'Friderik I.': ['Ulrik I.', 'Katarina', 'Herman I.', 'Ana Ortenburška'],
             'Friderik II.': ['Friderik III.', 'Ulrik II.'], 'Jurij': []}
            
            tests = [
                    ("najdaljsi_podpis('Friderik I.', rodovnikCG)", 'Ana Ortenburška', {'rodovnikCG': rodovnikCG}),
                    ("najdaljsi_podpis('Friderik II.', rodovnikCG)", 'Friderik III.', {'rodovnikCG': rodovnikCG}),
                    ("najdaljsi_podpis('Jurij', rodovnikCG)", 'Jurij', {'rodovnikCG': rodovnikCG}),
                    ("najdaljsi_podpis('Katarina', rodovnikCG)", 'Katarina', {'rodovnikCG': rodovnikCG}),
                    ("najdaljsi_podpis('Herman II.', rodovnikCG)", 'Friderik III.', {'rodovnikCG': rodovnikCG}),
                    ("najdaljsi_podpis('Ulrik I.', rodovnikCG)", 'Ana Celjska', {'rodovnikCG': rodovnikCG})
                    ]
            
            for expression, result, env in tests:
                if not Check.equal(expression, result, env=env):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoyMDE5OCwidXNlciI6MzM2N30:1h4LN5:R6-btgSRjS6jESg4ojWRUHekzrU'
        try:
            rodovnikCG = {
             'Ulrik I.': ['Viljem'], 'Margareta': [], 'Herman I.': ['Herman II.', 'Hans'],
             'Elizabeta II.': [], 'Viljem': ['Ana Celjska'], 'Elizabeta I.': [],
             'Ana Celjska': [], 'Herman III.': ['Margareta'], 'Ana Ortenburška': [],
             'Barbara': [], 'Herman IV.': [], 'Katarina': [], 'Friderik III.': [],
             'Herman II.': ['Ludvik', 'Friderik II.', 'Herman III.', 'Elizabeta I.', 'Barbara'],
             'Ulrik II.': ['Herman IV.', 'Jurij', 'Elizabeta II.'], 'Hans': [], 'Ludvik': [],
             'Friderik I.': ['Ulrik I.', 'Katarina', 'Herman I.', 'Ana Ortenburška'],
             'Friderik II.': ['Friderik III.', 'Ulrik II.'], 'Jurij': []}
            
            tests = [
                    ("najkrajse_ime('Friderik I.', rodovnikCG)", 'Ana', {'rodovnikCG': rodovnikCG}),
                    ("najkrajse_ime('Friderik II.', rodovnikCG)", 'Ulrik', {'rodovnikCG': rodovnikCG}),
                    ("najkrajse_ime('Jurij', rodovnikCG)", 'Jurij', {'rodovnikCG': rodovnikCG}),
                    ("najkrajse_ime('Katarina', rodovnikCG)", 'Katarina', {'rodovnikCG': rodovnikCG}),
                    ("najkrajse_ime('Herman II.', rodovnikCG)", 'Ulrik', {'rodovnikCG': rodovnikCG}),
                    ("najkrajse_ime('Ulrik I.', rodovnikCG)", 'Ana', {'rodovnikCG': rodovnikCG})
                    ]
            
            for expression, result, env in tests:
                if not Check.equal(expression, result, env=env):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoyMDE5OSwidXNlciI6MzM2N30:1h4LN5:buwaHttMGnKJxSN3x2kLtR2U3_c'
        try:
            rodovnikCG = {
             'Ulrik I.': ['Viljem'], 'Margareta': [], 'Herman I.': ['Herman II.', 'Hans'],
             'Elizabeta II.': [], 'Viljem': ['Ana Celjska'], 'Elizabeta I.': [],
             'Ana Celjska': [], 'Herman III.': ['Margareta'], 'Ana Ortenburška': [],
             'Barbara': [], 'Herman IV.': [], 'Katarina': [], 'Friderik III.': [],
             'Herman II.': ['Ludvik', 'Friderik II.', 'Herman III.', 'Elizabeta I.', 'Barbara'],
             'Ulrik II.': ['Herman IV.', 'Jurij', 'Elizabeta II.'], 'Hans': [], 'Ludvik': [],
             'Friderik I.': ['Ulrik I.', 'Katarina', 'Herman I.', 'Ana Ortenburška'],
             'Friderik II.': ['Friderik III.', 'Ulrik II.'], 'Jurij': []}
            
            tests = [
                    ("globina('Friderik I.', rodovnikCG)", 6, {'rodovnikCG': rodovnikCG}),
                    ("globina('Friderik II.', rodovnikCG)", 3, {'rodovnikCG': rodovnikCG}),
                    ("globina('Jurij', rodovnikCG)", 1, {'rodovnikCG': rodovnikCG}),
                    ("globina('Katarina', rodovnikCG)", 1, {'rodovnikCG': rodovnikCG}),
                    ("globina('Herman II.', rodovnikCG)", 4, {'rodovnikCG': rodovnikCG}),
                    ("globina('Ulrik I.', rodovnikCG)", 3, {'rodovnikCG': rodovnikCG})
                    ]
            
            for expression, result, env in tests:
                if not Check.equal(expression, result, env=env):
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
