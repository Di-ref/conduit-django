import json

from rest_framework.renderers import JSONRenderer

#from rest_framework.utils.serializer_helpers import ReturnList


class ConduitJSONRenderer(JSONRenderer):
    charset = 'utf-8'
    object_label = 'object'
    pagination_object_label = 'objects'
    pagination_count_label = 'count'

    def render(self, data, media_type=None, renderer_context=None):
    #     # If the view throws an error (such as the user can't be authenticated)
    #     # `data` will contain an `errors` key. We want
    #     # the default JSONRenderer to handle rendering errors, so we need to
    #     # check for this case.
    #     #errors = data.get('errors', None)

    #     if isinstance(data, ReturnList):
    #         listdata = super(ConduitJSONRenderer, self).render(data).decode('utf-8')
    #         _data = json.loads(listdata)
        if data.get('results', None) is not None:
            return json.dumps({
        #         self.object_label_plural: _data
        #     })
        # else:
        #     errors = data.get('error', None)
        #     if errors is not None:
        #         return super(ConduitJSONRenderer, self).render(data)
                self.pagination_object_label: data['results'],
               self.pagination_count_label: data['count']
           })
        elif data.get('errors', None) is not None:
            return super(ConduitJSONRenderer, self).render(data)

        else:
            return json.dumps({
                self.object_label: data
            })

        # if errors is not None:
        #     # As mentioned above, we will let the default JSONRenderer handle
        #     # rendering errors.
        #     return super(ConduitJSONRenderer, self).render(data)

        # return json.dumps({
        #     self.object_label: data
        # })
        