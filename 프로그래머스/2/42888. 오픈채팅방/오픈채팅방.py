def solution(record):
    messages = []
    answer = []
    dic = {}
    for r in record:
        arr = r.split(' ');
        command = arr[0];
        if command == 'Change':
            dic[arr[1]] = arr[2];
        else:
          if command == 'Enter':
            dic[arr[1]] = arr[2];
          messages.append([arr[0],arr[1]]);
    for message in messages:
        command = ''
        if message[1] in dic:
            nickname = dic[message[1]];
        if message[0] == 'Enter':
            command = '들어왔습니다.';
        else:
            command = '나갔습니다.';
        answer.append(nickname+'님이 '+command);
           
    return answer