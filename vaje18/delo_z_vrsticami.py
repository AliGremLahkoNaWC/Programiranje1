# =============================================================================
# Delo z vrsticami
# =====================================================================@019456=
# 1. podnaloga
# Sestavi funkcijo `prestej_vrstice(datoteka)`, ki prešteje, koliko vrstic je na
# dani znakovni datoteki. Funkcija naj za parameter dobi ime datoteke.
# =============================================================================
def prestej_vrstice(datoteka):
    '''presteje stevilo vrstic v datoteki'''
    stev = 0
    with open(datoteka, 'r') as dat:
        for vrstica in dat:
            stev += 1
    return stev
# =====================================================================@019457=
# 2. podnaloga
# Sestavi funkcijo `vrni_k_vrstico(datoteka, k)`, ki vrne k-to vrstico dane
# znakovne datoteke. Vrednost k in ime datoteke naj funkcija dobi za parameter.
# V primeru ko datoteka ne vsebuje dovolj vrstic, naj vrne prazen niz.
# =============================================================================
def vrni_k_vrstico(datoteka, k):
    '''vrne k-to vrstico'''
    stev = 0
    with open(datoteka, 'r') as dat:
        for vrstica in dat:
            stev += 1
            if stev == k:
                return vrstica
    return ''
# =====================================================================@019458=
# 3. podnaloga
# Na datoteki je pesem zapisana po kiticah. 
# To pomeni, da so med kiticami prazne vrstice. Sestavi
# funkcijo `odstrani_prazne_vrstice(datotekaV, datotekaI)`, ki bo 
# za dano ime datoteke `datotekaV` vse kitice združila in jih izpisala na
# datoteko `datotekaI`.
# <h5>datotekaV:</h5>
# 
#     Dekle je po vodo šlo
#     na visoke planine.
# 
#     Vodo je zajemala,
#     je ribico zajela.
#     
#     Ribica jo je prosila:
#     oj, pusti me živeti.
#     
#     Dekle b'la je usmiljena,
#     je ribico spustila.
#     
#     Ribica je zaplavala,
#     je dekle poškropila.
# 
# <h5>DatotekaI:</h5>
# 
#     Dekle je po vodo šlo
#     na visoke planine.
#     Vodo je zajemala,
#     je ribico zajela.
#     Ribica jo je prosila:
#     oj, pusti me živeti.
#     Dekle b'la je usmiljena,
#     je ribico spustila.
#     Ribica je zaplavala,
#     je dekle poškropila.
# =============================================================================
def odstrani_prazne_vrstice(datotekaV,datotekaI):
    '''odstrani presledke v pesmi'''
    pisanje = open('datotekaI.txt','w+')
    with open(datotekaV, 'r') as dat:
        for vrstica in dat:
            
            if vrstica[0].isalpha():
                print(vrstica,file=pisanje,end='\n')
            else:
                pass
        pisanje.close()
        
    return pisanje
# =====================================================================@019459=
# 4. podnaloga
# Direktor podjetja je dobil datoteko `priporocilo.txt` na kateri je pisalo:
# Spoštovani gospod direktor,
# 
#     Janeza Novaka, mojega asistenta pri delu, vedno vidite, kako
#     trdo dela v svoji mali pisarni. Janez dela neodvisno in ne
#     lenari ali se pogovarja s sodelovci. Nikoli se ne zgodi, da bi
#     zavrnil kakšnega sodelovca, ki potrebuje pomoc. Do sedaj je vedno
#     koncal z delom pravocasno. Zelo pogosto si vzeme podaljšan
#     delovni cas, da konca svoje delo, pri cemer vcasih preskoci
#     odmor. Janez je takšen delavec, ko nima absolutno nobenega
#     spodrslajaja pri opravljenih delih, ima visoke dosežke in je širokega
#     znanja na njegovem podrocju. Moje mnenje je, da ga lahko takoj
#     uvrstimo med tiste najbolj vzorne delovce, ki jih nikoli ne
#     odpustimo. Prav tako vam vljudno predlagam, da je moj predlog
#     o napredovanju tega izjemnega, vzornega in nepogrešljivega delavca
#     izvršen kakor hitro je mogoce.
#     
#     Lep pozdrav!
# 
# <i>Že se je spravil pisati predlog za napredovanje, ko je po e-pošti prispel dopis:</i>
# 
#     Direktor!
#     Ta idiot je stal za menoj, ko sem pisal prejšnje priporocilo.
#     Prosim znova preberite vsako drugo vrstico tega pisma.
# 
# Direktor je sedaj povsem zmeden. Pomagaj mu in sestavi funkcijo
# `izpisi_drugo(datotekaV, datotekaI)`, ki na `datotekoI` izpiše vsako drugo vrstico
# vsebine datoteke `datotekaV`!
# =============================================================================
def izpisi_drugo(datotekaV,datotekaI):
    '''funkcija prepiše vsako 2. vrstico iz prve datoteke v drugo'''
    popravljeno = open('datotekaI.txt','w+')
    with open(datotekaV, 'r') as dat:
        i = 0
        for vrstica in dat:
            if i%2 == 0:
                i += 1
                pass
            else:
                print(vrstica,file=popravljeno,end='\n')
                i += 1
        popravljeno.close()
    return datotekaI



































































































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
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxOTQ1Nn0:1h9Que:924X59XM6EIyt99uWbBiF9BeTEs'
        try:
            with Check.in_file("priporocilo.txt",[
            "Janeza Novaka, mojega asistenta pri delu, vedno vidite, kako",
            "trdo dela v svoji mali pisarni. Janez dela neodvisno in ne",
            "lenari ali se pogovarja s sodelovci. Nikoli se ne zgodi, da bi",
            "zavrnil kakšnega sodelovca, ki potrebuje pomoc. Do sedaj je vedno",
            "koncal z delom pravocasno. Zelo pogosto si vzeme podaljšan",
            "delovni cas, da konca svoje delo, pri cemer vcasih preskoci",
            "odmor. Janez je takšen delavec, ko nima absolutno nobenega",
            "spodrslajaja pri opravljenih delih, ima visoke dosežke in je širokega",
            "znanja na njegovem podrocju. Moje mnenje je, da ga lahko takoj",
            "uvrstimo med tiste najbolj vzorne delovce, ki jih nikoli ne",
            "odpustimo. Prav tako vam vljudno predlagam, da je moj predlog",
            "o napredovanju tega izjemnega, vzornega in nepogrešljivega delavca",
            "izvršen kakor hitro je mogoce.",
            "",
            "Lep pozdrav!"
            ]):
                Check.equal('prestej_vrstice("priporocilo.txt")', 15)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxOTQ1N30:1h9Que:aRLvWCquYgfmV8isgFhcDUX09xg'
        try:
            with open("priporocilo.txt", "w") as test_f:
                for vr in [
                    "Janeza Novaka, mojega asistenta pri delu, vedno vidite, kako",
                    "trdo dela v svoji mali pisarni. Janez dela neodvisno in ne",
                    "lenari ali se pogovarja s sodelovci. Nikoli se ne zgodi, da bi",
                    "zavrnil kakšnega sodelovca, ki potrebuje pomoc. Do sedaj je vedno",
                    "koncal z delom pravocasno. Zelo pogosto si vzeme podaljšan",
                    "delovni cas, da konca svoje delo, pri cemer vcasih preskoci",
                    "odmor. Janez je takšen delavec, ko nima absolutno nobenega",
                    "spodrslajaja pri opravljenih delih, ima visoke dosežke in je širokega",
                    "znanja na njegovem podrocju. Moje mnenje je, da ga lahko takoj",
                    "uvrstimo med tiste najbolj vzorne delovce, ki jih nikoli ne",
                    "odpustimo. Prav tako vam vljudno predlagam, da je moj predlog",
                    "o napredovanju tega izjemnega, vzornega in nepogrešljivega delavca",
                    "izvršen kakor hitro je mogoce.",
                    "",
                    "Lep pozdrav!"]:
                    print(vr, file=test_f)
            Check.equal('vrni_k_vrstico("priporocilo.txt",4)', "zavrnil kakšnega sodelovca, ki potrebuje pomoc. Do sedaj je vedno\n")
            Check.equal('vrni_k_vrstico("priporocilo.txt",50)', "")
            Check.equal('vrni_k_vrstico("priporocilo.txt",15)', "Lep pozdrav!\n")
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxOTQ1OH0:1h9Que:K7xguU8ysIzwPl0gNWnD4PLW-uk'
        try:
            with Check.in_file("dekle.txt", [
                    "Dekle je po vodo šlo",
                    "na visoke planine.",
                    "",
                    "Vodo je zajemala,",
                    "je ribico zajela. ",
                    "",  
                    "Ribica jo je prosila:",
                    "oj, pusti me živeti.",
                    "",
                    "Dekle b'la je usmiljena,",
                    "je ribico spustila.",
                    "",
                    "Ribica je zaplavala,",
                    "je dekle poškropila.",
                    "",
                    "",
                    ""
                    ]):
                odstrani_prazne_vrstice("dekle.txt", "dekle_out.txt")
                Check.out_file("dekle_out.txt", [
                    "Dekle je po vodo šlo",
                    "na visoke planine.",
                    "Vodo je zajemala,",
                    "je ribico zajela. ",
                    "Ribica jo je prosila:",
                    "oj, pusti me živeti.",
                    "Dekle b'la je usmiljena,",
                    "je ribico spustila.",
                    "Ribica je zaplavala,",
                    "je dekle poškropila."
                    ])
                
            with Check.in_file("dekle1.txt", [
                    "",
                    "",
                    "Dekle je po vodo šlo",
                    "na visoke planine.",
                    "",
                    "Vodo je zajemala,",
                    "je ribico zajela. ",
                    "",  
                    "Ribica jo je prosila:",
                    "oj, pusti me živeti.",
                    "",
                    "Dekle b'la je usmiljena,",
                    "je ribico spustila.",
                    "",
                    "Ribica je zaplavala,",
                    "je dekle poškropila.",
                    "",
                    "",
                    ""
                    ]):
                odstrani_prazne_vrstice("dekle1.txt", "dekle_out1.txt")
                Check.out_file("dekle_out1.txt", [
                    "Dekle je po vodo šlo",
                    "na visoke planine.",
                    "Vodo je zajemala,",
                    "je ribico zajela. ",
                    "Ribica jo je prosila:",
                    "oj, pusti me živeti.",
                    "Dekle b'la je usmiljena,",
                    "je ribico spustila.",
                    "Ribica je zaplavala,",
                    "je dekle poškropila."
                    ])
            with Check.in_file("dekle2.txt", [
                    "",
                    "",
                    "Dekle je po vodo šlo",
                    "na visoke planine.",
                    "",
                    "Vodo je zajemala,",
                    "je ribico zajela. ",
                    "",
                    ""
                    "Ribica jo je prosila:",
                    "oj, pusti me živeti.",
                    "",
                    "Dekle b'la je usmiljena,",
                    "je ribico spustila.",
                    "",
                    "",
                    "Ribica je zaplavala,",
                    "je dekle poškropila.",
                    "",
                    "",
                    ""
                    ]):
                odstrani_prazne_vrstice("dekle2.txt", "dekle_out2.txt")
                Check.out_file("dekle_out2.txt", [
                    "Dekle je po vodo šlo",
                    "na visoke planine.",
                    "Vodo je zajemala,",
                    "je ribico zajela. ",
                    "Ribica jo je prosila:",
                    "oj, pusti me živeti.",
                    "Dekle b'la je usmiljena,",
                    "je ribico spustila.",
                    "Ribica je zaplavala,",
                    "je dekle poškropila."
                    ])
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxOTQ1OX0:1h9Que:rXcsHQkt_Nh8Tooj_sdSTCs5Cck'
        try:
            with Check.in_file("izp2.txt", [
                    "Janeza Novaka, mojega asistenta pri delu, vedno vidite, kako",
                    "trdo dela v svoji mali pisarni. Janez dela neodvisno in ne",
                    "lenari ali se pogovarja s sodelovci. Nikoli se ne zgodi, da bi",
                    "zavrnil kakšnega sodelovca, ki potrebuje pomoc. Do sedaj je vedno",
                    "koncal z delom pravocasno. Zelo pogosto si vzeme podaljšan",
                    "delovni cas, da konca svoje delo, pri cemer vcasih preskoci",
                    "odmor. Janez je takšen delavec, ko nima absolutno nobenega",
                    "spodrslajaja pri opravljenih delih, ima visoke dosežke in je širokega",
                    "znanja na njegovem podrocju. Moje mnenje je, da ga lahko takoj",
                    "uvrstimo med tiste najbolj vzorne delovce, ki jih nikoli ne",
                    "odpustimo. Prav tako vam vljudno predlagam, da je moj predlog",
                    "o napredovanju tega izjemnega, vzornega in nepogrešljivega delavca",
                    "izvršen kakor hitro je mogoce.",
                    "",
                    "Lep pozdrav!"]):
                    izpisi_drugo("izp2.txt", "izp2-rez.txt")
                    Check.out_file("izp2-rez.txt", [
                    "Janeza Novaka, mojega asistenta pri delu, vedno vidite, kako",
                    "lenari ali se pogovarja s sodelovci. Nikoli se ne zgodi, da bi",
                    "koncal z delom pravocasno. Zelo pogosto si vzeme podaljšan",
                    "odmor. Janez je takšen delavec, ko nima absolutno nobenega",
                    "znanja na njegovem podrocju. Moje mnenje je, da ga lahko takoj",
                    "odpustimo. Prav tako vam vljudno predlagam, da je moj predlog",
                    "izvršen kakor hitro je mogoce.",
                    "Lep pozdrav!"])
            
            
            with Check.in_file("izp1.txt", [
                    "12",
                    "2",
                    "3"]):
                    izpisi_drugo("izp1.txt", "izp1-rez.txt")
                    Check.out_file("izp1-rez.txt", [
                    "12",
                    "3"])
            
            with Check.in_file("izp3.txt", [
                    "12",
                    "3"]):
                    izpisi_drugo("izp3.txt", "izp3-rez.txt")
                    Check.out_file("izp3-rez.txt", [
                    "12"])
                    
            with Check.in_file("izp4.txt", [
                    "12",
                    "",
                    "",
                    "",
                    "333",
                    "1",
                    "2",
                    "2",
                    "3"]):
                    izpisi_drugo("izp4.txt", "izp4-rez.txt")
                    Check.out_file("izp4-rez.txt", [
                    "12",
                    "",
                    "333",
                    "2",
                    "3"])
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
