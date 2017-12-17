import codecs
import sys

# braille_mappings.csv stolen gratefully from https://raw.githubusercontent.com/markomanninen/pybrl/master/braille_mappings.csv
# MIT licence:
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
with codecs.open('braille_mappings.csv', 'r', encoding='utf-8') as f:
	d = {}
	for line in f.readlines():
		p = line.split(',')
		letter = p[2]
		dots = p[3]
		d[dots] = letter
	lines = sys.stdin.readlines()
	for i in range(0, len(lines[0])//3):
		dots = []
		if lines[0][i*3] == '.':
			dots.append(1)
		if lines[1][i*3] == '.':
			dots.append(2)
		if lines[2][i*3] == '.':
			dots.append(3)
		if lines[0][i*3 + 1] == '.':
			dots.append(4)
		if lines[1][i*3 + 1] == '.':
			dots.append(5)
		if lines[2][i*3 + 1] == '.':
			dots.append(6)
		k = '-'.join(str(c) for c in dots)
		print(d[k], end='')
