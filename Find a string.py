def count_substring(A,X):
    count = 0
    for i in range(len(A)-len(X)+1):
        if(A[i:i+len(X)]==X):
            count+=1
    return count
                   

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)