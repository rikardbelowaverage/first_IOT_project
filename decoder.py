import base64

def format_payload(args):

    # Log received data for debugging purposes:
    print(args)
    
    # See Helium's default JSON schema at: https://developer.helium.com/console/integrations/json-schema

    # Get RSSI and SNR variables using Helium hotspots data:
    hotspots = args.get('hotspots', [])
    ubidots_payload = {}

    for i in range(len(hotspots)):
        hotspot_name = hotspots[i].get('name', '')
        rssi = hotspots[i].get('rssi', '')
        snr = hotspots[i].get('snr', '')

        # Use reported timestamp of each hotspot
        ts = int(hotspots[i].get('reported_at', ""))
        
        # Delete no longer needed keys from payload, and assign to context
        hotspots[i].pop('rssi', None)
        hotspots[i].pop('snr', None)
        hotspots[i].pop('reported_at', None)
        hotspot_context = hotspots[i]

        # Format payload for RSSI and SNR
        ubidots_payload['rssi-' + hotspot_name] = {'value': rssi, 'timestamp': ts, 'context': hotspot_context}
        ubidots_payload['snr-' + hotspot_name] = {'value': snr, 'timestamp': ts}
    
    # Get Fcnt and Port variables:
    ubidots_payload['fcnt'] = args.get('fcnt', None)
    ubidots_payload['port'] = args.get('port', None)
    
    # Get main payload's timestamp
    ubidots_payload['timestamp'] = int(args.get('reported_at', ""))
    
    # See if there's a decoded payload already
    decoded_payload = args.get('decoded', {}).get('payload', {})

    # If no decoded payload was found, then decode here:
    if not bool(decoded_payload):
        bytes = base64.b64decode(args.get('payload', ''))
        
        # This a sample decoder for RAK1906 WisBlock Environmental Sensor (https://docs.rakwireless.com/Product-Categories/WisBlock/RAK1906/Overview/#)
        if bytes[0] == 1:
            decoded_payload['temperature'] = (bytes[0] << 24 >> 16 | bytes[1]) / 100
            decoded_payload['humidity'] = (bytes[2])
            #decoded_payload['pressure'] = (bytes[3])
        else:
            decoded_payload['temperature'] = (bytes[0] << 24 >> 16 | bytes[1]) / 100
            decoded_payload['humidity'] = (bytes[2])
            #decoded_payload['pressure'] = (bytes[3])
            
    # Join dicts into Ubidots payload
    ubidots_payload.update(decoded_payload)

    return ubidots_payload
