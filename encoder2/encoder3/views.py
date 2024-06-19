# views.py

from django.shortcuts import render
from .forms import EncodeMessageForm
from .utils import encode_message, get_encoding_mapping

def encode_message_view(request):
    if request.method == 'POST':
        form = EncodeMessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            
            # Get encoding mappings for both odd and even days
            odd_encoding = encode_message(message, 'odd')
            even_encoding = encode_message(message, 'even')
            
            return render(request, 'mains/result.html', {
                'odd_encoded_message': odd_encoding,
                'even_encoded_message': even_encoding,
            })
    else:
        form = EncodeMessageForm()

    return render(request, 'mains/encode_message.html', {'form': form})
