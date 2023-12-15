def prod_non_zero_diag(a, n):
    ans = 1
    for j in range(n):
        if (a[j][j] != 0):
            ans *= a[j][j]
    return ans


def are_multisets_equal(x, y):
      return sorted(x) == sorted(y)


def max_after_zero(a, n):
    ans = -1
    for i in range(1, n):
        if (a[i - 1] == 0):
            ans = max(ans, a[i])
    return ans


def convert_image(img, coefs):
    image = []
    for i in range(len(img)):
        image.append([])
        for j in range(len(img[i])):
            image[-1].append(img[i][j] * coefs[0] +
                     img[i][j] * coefs[1] +
                     img[i][j] * coefs[2])
    return image


def run_length_encoding(x, n):
    fir = [x[0]]
    sec = [1]
    for i in range(1, n-1):
        if (x[i-1] == x[i]):
            sec[-1]+=1
        else:
            fir.append(x[i])
            sec.append(2)
    return fir, sec

def pairwise_distance(x, y):
    m = []
    for i in range(len(x)):
        m.append([])
        for j in range(len(y)):
            m[-1].append(((x[i][0] - y[i][0]) ** 2 + (x[i][1] - y[i][1]) ** 2) ** 0.5)
    return m;
            
            
            
            
            