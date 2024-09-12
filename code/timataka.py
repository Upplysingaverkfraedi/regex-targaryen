import requests
import pandas as pd
import argparse
import re 


def parse_arguments():
    parser = argparse.ArgumentParser(description='Vinna með úrslit af tímataka.net.')
    parser.add_argument('--url', help='Slóð að vefsíðu með úrslitum.')
    parser.add_argument('--output', required=True,
                        help='Slóð að útgangsskrá til að vista niðurstöðurnar (CSV format).')
    parser.add_argument('--debug', action='store_true',
                        help='Vistar html í skrá til að skoða.')
    return parser.parse_args()


def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Tókst ekki að sækja gögn af {url}")
        return None


def parse_html(html):
    pattern = r'<tr>\s*<td class="hidden-xs">(\d+)</td>\s*<td>(\d+)</td>\s*<td>Þorlákur Rafnsson</td>\s*<td class="hidden-xs">(\d+)</td>\s*<td class="hidden-xs">(.*?)</td>\s*<td>(.*?)<br></td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>'
        # Nota re.findall til að finna allar samsvaranir
    matches = re.findall(pattern, html)

    # Breyta niðurstöðum yfir í lista af dicts til að auðvelda skráningu í csv
    # Með match[0], match[1]... erum við að sækja réttu gögn frá reglulegu segðinni. Því þau raðast í þessa röð. 

    results = []
    for match in matches:
        results.append({
            'Rank': match[0],
            'BIB': match[1],
            'Name': 'Þorlákur Rafnsson', # þetta er fasti því við erum að skoða gögn frá Þorláki
            'Year': match[2],
            'Club': match[3],
            'Split': match[4],
            'Time': match[5],
            'Behind': match[6],
            'Chiptime': match[7]
        })

    return results


def skrifa_nidurstodur(data, output_file):
    """
    Skrifar niðurstöður í úttaksskrá.
    :param data:        (list) Listi af línum
    :param output_file: (str) Slóð að úttaksskrá
    :return:            None
    """
    if not data:
        print("Engar niðurstöður til að skrifa.")
        return

    df = pd.DataFrame(data)
    df.to_csv(output_file, sep=',', index=False)
    print(f"Niðurstöður vistaðar í '{output_file}'.")


def main():
    args = parse_arguments()

    if not args.output.endswith('.csv'):
        print(f"Inntaksskráin {args.output} þarf að vera csv skrá.")
        return

    if not 'timataka.net' in args.url:
        # Regluleg segð til að passa að URL-ið sé úrslitasíða af timataka.net

        url_pattern = r'https://(www\.)?timataka\.net/.+/urslit/\?race=\d+.*'
        print("Slóðin er ekki frá timataka.net")
        return

    html = fetch_html(args.url)
    if not html:
        raise Exception("Ekki tókst að sækja HTML gögn, athugið URL.")

    if args.debug:
        html_file = args.output.replace('.csv', '.html')
        with open(html_file, 'w') as file:
            file.write(html)
        print(f"HTML fyrir {args.url} vistað í {html_file}")

    results = parse_html(html)
    skrifa_nidurstodur(results, args.output)


if __name__ == "__main__":
    main()
