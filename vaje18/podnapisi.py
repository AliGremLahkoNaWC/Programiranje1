# =============================================================================
# Podnapisi
#
# S tekmovanja RTK 2006
# =====================================================================@020323=
# 1. podnaloga
# Nek predvajalnik filmov bi radi dopolnili tako, da bo znal prikazovati tudi 
# podnapise. Te imamo podane v samostojnih datotekah, ločeno od filma, tako da 
# lahko k istemu filmu pritaknemo podnapise v različnih jezikih. Ob predvajanju 
# je treba, tik preden se prikaže posamezna sličica filma, ugotoviti, kateri 
# podnapis pripada tej sličici (če sploh kakšen).
# 
# #### Naloga
# Dopolni funkcijo `podnapisi(txt, cas_slicice)`, ki jo bo sistem poklical pred
# prikazom vsake sličice, funkcija pa bo vrnila podnapis, ki ga je treba
# prikazati na tej sličici (oz. prazen niz, če ni treba prikazati nobenega
# podnapisa). Uporabljeno naj bo utf-8 kodiranje.   
# Mesto dopolnjevanja je označeno z ###.
# 
#     def podnapisi(txt, cas_slicice):
#         """Iz datoteke txt izpiše podnapis, ki v filmu priprada sličici s številko st_slicice."""
#     
#         with open(txt, 'r', encoding=###) as podnapisi:
#             pravi_podnapis = False
#             for vrstica in podnapisi:
#                 if ###:
#                     vrstica = vrstica.strip()
#                     return vrstica
#     
#                 if ### in vrstica:
#                     zacetek, konec = vrstica.split(###)
#     
#                 if zacetek <= cas_slicice ###:
#                     pravi_podnapis = True
#             return ###
# 
# ##### Primer podnapisov
# Datoteka s podnapisi izgleda kot je prikazano spodaj. Najprej je naveden
# časovni interval v katerem je prikazan podnapis in nato še dejanski podnapis.
# Sledi prazna vrstica. Privzameš lahko, da noben podnapis ni podan v dveh
# vrsticah.
# 
#     00:01:32,416 --> 00:01:34,788
#     Ne smete govoriti?
#     
#     00:01:34,919 --> 00:01:36,081
#     Lahko govorimo.
#     
#     00:01:36,211 --> 00:01:39,960
#     A tako. Torej gre zame? –Bojijo se vas.
# 
# #### Vhodni podatki
# Datoteka s podnapisi in čas sličice ob katerem se ta prikaže v filmu.
# 
# #### Izhodni podatki
# Podnapis, ki ustreza sličici.
# 
# #### Primer
# 
#     >>> podnapisi('podnapisi1.txt','00:02:31,505')
#     'Pohiti. Ne spreminjaj nastavitev.'
# =============================================================================
def podnapisi(txt, cas_slicice):
    """Iz datoteke txt izpiše podnapis, ki v filmu priprada sličici s številko st_slicice."""
    zacetek = ''
    konec = '' 
    with open(txt, 'r', encoding='utf-8') as podnapisi:
        pravi_podnapis = False
        for vrstica in podnapisi:
            if pravi_podnapis:
                vrstica = vrstica.strip()
                return vrstica

            if ' --> ' in vrstica:
                zacetek, konec = vrstica.split(' --> ')

            if zacetek <= cas_slicice <= konec:
                pravi_podnapis = True
        return ''




































































































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
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoyMDMyM30:1h9Pak:5zGkPDRhPSEl8RWutw93e_n4_Wg'
        try:
            with Check.in_file('podnapisi1.txt', [
                                "00:00:54,087 --> 00:00:56,126",
                                "Provinca Kunar, Afganistan",
                                "",
                                "00:01:27,078 --> 00:01:28,821",
                                "Zdi se mi, kot da me peljete na vojaško sodišče.",
                                "",
                                "00:01:30,873 --> 00:01:32,284",
                                "Ali pa, da boste ustavili in me počili.",
                                "",
                                "00:01:32,416 --> 00:01:34,788",
                                "Ne smete govoriti?",
                                "",
                                "00:01:34,919 --> 00:01:36,081",
                                "Lahko govorimo.",
                                "",
                                "00:01:36,211 --> 00:01:39,960",
                                "A tako. Torej gre zame? –Bojijo se vas.",
                                "",
                                "00:01:40,090 --> 00:01:43,210",
                                "Ljubi bog, ženska ste. Nisem opazil.",
                                "",
                                "00:01:43,343 --> 00:01:45,751",
                                "Opravičil bi se, ampak to hočete, ne?",
                                "",
                                "00:01:45,888 --> 00:01:48,639",
                                "Zame ste vojak. –Pri letalstvu sem.",
                                "",
                                "00:01:48,765 --> 00:01:50,473",
                                "Odlično okostje imate.",
                                "",
                                "00:01:50,601 --> 00:01:53,352",
                                "Moram gledati.",
                                "",
                                "00:01:53,478 --> 00:01:56,183",
                                "Je to čudno? Kar smejte se.",
                                "",
                                "00:01:56,648 --> 00:01:59,104",
                                "Nekaj bi vprašal. –Kar.",
                                "",
                                "00:01:59,234 --> 00:02:02,899",
                                "Ste dobili vseh 12 modelov z naslovnice Maxima?",
                                "",
                                "00:02:03,029 --> 00:02:05,105",
                                "Odlično vprašanje. Ja in ne.",
                                "",
                                "00:02:05,240 --> 00:02:06,651",
                                "Z marcem nisva prišla skupaj,",
                                "",
                                "00:02:06,783 --> 00:02:09,654",
                                "na decembrski naslovnici pa sta dvojčici.",
                                "",
                                "00:02:09,786 --> 00:02:12,621",
                                "Še kaj? Ne hecaj se z dvigom roke.",
                                "",
                                "00:02:12,747 --> 00:02:16,579",
                                "Je kul, če se slikam z vami? –Ja. Zelo kul.",
                                "",
                                "00:02:21,631 --> 00:02:25,383",
                                "Na tvoji MySpace strani nočem videti znakov tolp.",
                                "",
                                "00:02:25,510 --> 00:02:27,052",
                                "Kar daj. Hecam se.",
                                "",
                                "00:02:27,178 --> 00:02:30,095",
                                "Obožujem mir. V miru bi bil brez dela.",
                                "",
                                "00:02:30,306 --> 00:02:34,256",
                                "Pohiti. Ne spreminjaj nastavitev.",
                                "",
                                "00:02:39,899 --> 00:02:41,938",
                                "Kaj se dogaja? –Stik levo!",
                                "",
                                "00:02:42,067 --> 00:02:43,692",
                                "Kaj je?",
                                "",
                                "00:02:44,987 --> 00:02:47,026",
                                "Jimmy, ostani s Starkom!",
                                "",
                                "00:02:47,156 --> 00:02:48,270",
                                "Skrijte se!",
                                "",
                                "00:02:54,538 --> 00:02:56,032",
                                "Porkaš!",
                                "",
                                "00:02:57,708 --> 00:03:00,495",
                                "Čakaj! –Ostanite tu!",
                                "",
                                "00:04:22,040 --> 00:04:23,285",
                                "Las Vegas, 36 ur prej",
                                "",
                                "00:04:23,416 --> 00:04:25,789",
                                "<i>Vizionar. Genij.</i>",
                                "",
                                "00:04:26,670 --> 00:04:28,543",
                                "<i>Ameriški domoljub.</i>",
                                "",
                                "00:04:29,881 --> 00:04:32,289",
                                "<i>Sin legendarnega izdelovalca orožja Howarda Starka</i>",
                                "",
                                "00:04:32,425 --> 00:04:35,960",
                                "<i>je že zgodaj opozoril nase s svojo pametjo.</i>",
                                "",
                                "00:04:36,090 --> 00:04:38,751",
                                "<i>Pri štirih letih je sestavil svoje prvo tiskano vezje.</i>",
                                "",
                                "00:04:39,060 --> 00:04:41,931",
                                "<i>Pri šestih pa svoj prvi motor.</i>",
                                "",
                                "00:04:42,352 --> 00:04:46,219",
                                "<i>Pri 17 letih pa je summa cum laude diplomiral na MIT.</i>",
                                "",
                                "00:04:47,231 --> 00:04:49,604",
                                "<i>Potem pa titan premine.</i>",
                                "",
                                "00:04:51,235 --> 00:04:54,106",
                                "<i>Howardov prijatelj O. Stane</i>",
                                "",
                                "00:04:54,238 --> 00:04:57,607",
                                "<i>zapolni praznino po legendarnem ustanovitelju,</i>",
                                "",
                                "00:04:57,867 --> 00:05:01,152",
                                "<i>dokler se pri 21 letih izgubljeni sin ne vrne</i>",
                                "",
                                "00:05:01,287 --> 00:05:04,620",
                                "<i>in postane direktor podjetja.</i>",
                                "",
                                "00:05:06,167 --> 00:05:08,918",
                                "<i>S Tonyjem se začne nova era,</i>",
                                "",
                                "00:05:09,044 --> 00:05:13,042",
                                "<i>saj ustvari 'pametno' orožje, robotiko, satelitsko iskanje.</i>",
                                "",
                                "00:05:13,173 --> 00:05:17,005",
                                "<i>Tony Stark je spremenil orožarsko industrijo,</i>",
                                "",
                                "00:05:17,136 --> 00:05:19,887",
                                "<i>saj zagotavlja svobodo, ščiti Ameriko</i>",
                                "",
                                "00:05:20,013 --> 00:05:22,504",
                                "<i>in njene interese po vsem svetu.</i>",
                                "",
                                "00:05:30,899 --> 00:05:33,188",
                                "Kot zveza s Stark Industries",
                                "",
                                "00:05:33,860 --> 00:05:37,525",
                                "sem služil z domoljubom,",
                                "",
                                "00:05:37,739 --> 00:05:41,357",
                                "ki je moj prijatelj in mentor."], encoding='utf-8'):
            
                Check.equal("podnapisi('podnapisi1.txt','00:01:52,605')", 'Moram gledati.')
                Check.equal("podnapisi('podnapisi1.txt','00:04:22,040')", 'Las Vegas, 36 ur prej')
                Check.equal("podnapisi('podnapisi1.txt','00:05:04,620')", '<i>in postane direktor podjetja.</i>')
                Check.equal("podnapisi('podnapisi1.txt','00:05:04,621')", '')
                Check.secret(podnapisi('podnapisi1.txt', '00:01:41,095'))
                Check.secret(podnapisi('podnapisi1.txt', '01:00:05,205'))
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
