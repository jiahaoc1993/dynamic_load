import tarfile
import io


class ArchiveImporter:
    def __init__(self, modules: dict = None, path: str = ''):
        self._modules = modules
        self._path = path
    
    def extract_content(self, path):
        tar_obj = _get_archive_obj(path)
        tar_obj.extractall(self._path)


def _get_archive_obj(path):
    archive_file = open(path, 'rb')
    archive_io  = io.BytesIO(archive_file.read())
    tar = tarfile.open(fileobj=archive_io, mode='r:*')
    return tar


def _list_archive(archive_obj):
    return archive_obj.getnames()


#    def find_module(self, fullname, path=None):


if __name__ == '__main__':
    importer = ArchiveImporter(['text'], './test')
    #tar_obj = _get_archive_obj('./test.tar')
    #print(_list_archive(tar_obj))
    importer.extract_content('./test.tar')
