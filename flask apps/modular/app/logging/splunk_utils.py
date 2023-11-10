def request_msg(request):
    method = request.method
    qprms = repr(request.query_string)
    hdrs = filter(lambda hdr: hdr[0].upper().startswith('X-') , request.headers)
    hdr_txt = ['{0}: {1}'.format(repr(x[0]), repr(x[1])) for x in hdrs]
    data = repr(request.data)
    end_pnt = request.path
    msg = f'end_point={end_pnt} | req_method={method} req_headers={repr(hdr_txt)} req_params=[{qprms}] req_data={data}'
    return msg