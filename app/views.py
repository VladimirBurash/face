import base64
import hashlib
import json

import numpy
from PIL import Image
from skimage import io

import numpy as np
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from scipy.spatial import distance

from app import DETECTOR, SP, FACEREC
from app.models import Person
from app.utils import get_descriptor
import io as ios

class BadRequest(Exception):
    pass


@method_decorator(csrf_exempt, name='dispatch')
class CheckImage(View):
    def post(self, request):
        try:
            data = json.loads(request.body.decode('utf-8')).get('data').split(',')[1]
        except:
            raise BadRequest('bad_json')
        data_decoded = base64.b64decode(data)
        image = Image.open(ios.BytesIO(data_decoded))
        ar = numpy.array(image)
        dets = DETECTOR(ar, 1)
        for k, d in enumerate(dets):
            shape = SP(ar, d)
        if shape:
            desc = FACEREC.compute_face_descriptor(ar, shape)
            persons = Person.objects.all()
            for p in persons:
                if p.descriptor:
                    p_desc = np.fromstring(p.descriptor, sep='\n')
                    a = distance.euclidean(desc, p_desc)
                    if a < 0.5:
                        return {
                            'person': p.name,
                        }
        return {
            'status': False
        }
