"""
    OVERALL CREDIT TO:
        t0mm0, Eldorado, VOINAGE, BSTRDMKR, tknorris, smokdpi, TheHighway

    Plugin for ResolveURL
    Copyright (C) 2011 t0mm0

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from resolveurl.plugins.__resolve_generic__ import ResolveGeneric
from resolveurl.plugins.lib import helpers


class DatoPornResolver(ResolveGeneric):
    name = "datoporn"
    domains = ['datoporn.com', 'dato.porn', 'datoporn.co']
    pattern = r'(?://|\.)(datoporn\.com|dato\.porn|datoporn\.co)/(?:embed[/-]|emb.html\?)?([0-9a-zA-Z]+)'

    def get_media_url(self, host, media_id):
        return helpers.get_media_url(self.get_url(host, media_id), patterns=[r'''video_url:\s*'(?P<url>[^']+)'''])

    def get_url(self, host, media_id):
        return self._default_get_url(host, media_id, template='https://dato.porn/embed/{media_id}/')

    @classmethod
    def _is_enabled(cls):
        return True
