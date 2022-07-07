from setting import *
import matplotlib.pyplot as plt
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


def plotting():
    plt.figure(1)
    plt.plot(records['iterations'], records['err_train'],
             label='error per hundred iterations')
    min_index = int(np.argmin(records['err_train']))
    mini = records['err_train'][min_index]
    plt.plot(min_index * 100, mini, color=color1, marker='o',
             markersize=5, label='error minimum: ' + str(np.round(mini, 5)))
    plt.title(choice.upper() + '  Train Error', fontsize=font2)
    plt.legend(loc='upper right')
    plt.xlabel('Number of iterations', fontsize=font3)
    plt.ylabel('Error value', fontsize=font3)
    plt.tight_layout()
    plt.savefig('C:/Users/86187/Documents/GitHub/Weiczh-s-1st/hw3/figures/' +
                str(choice) + '_train_err.png')
    # plt.show()
    plt.close()

    plt.figure(2)
    plt.plot(records['iterations'], records['err_test'],
             label='error per hundred iterations')
    min_index = int(np.argmin(records['err_test']))
    mini = records['err_test'][min_index]
    plt.plot(min_index * 100, mini, color=color1, marker='o',
             markersize=5, label='error minimum: ' + str(np.round(mini, 5)))
    plt.title(choice.upper() + '  Test Error', fontsize=font2)
    plt.legend(loc='upper right')
    plt.xlabel('Number of iterations', fontsize=font3)
    plt.ylabel('Error value', fontsize=font3)
    plt.tight_layout()
    plt.savefig('C:/Users/86187/Documents/GitHub/Weiczh-s-1st/hw3/figures/' +
                str(choice) + '_test_err.png')
    # plt.show()
    plt.close()

    plt.figure(3)
    plt.plot(records['iterations'], records['loss_train'],
             label='loss per hundred iterations')
    min_index = int(np.argmin(records['loss_train']))
    mini = records['loss_train'][min_index]
    plt.plot(min_index * 100, mini, color=color1, marker='o',
             markersize=5, label='loss minimum: ' + str(np.round(mini, 5)))
    plt.title(choice.upper() + '  Train Loss', fontsize=font2)
    plt.legend(loc='upper right')
    plt.xlabel('Number of iterations', fontsize=font3)
    plt.ylabel('Loss value', fontsize=font3)
    plt.tight_layout()
    plt.savefig('C:/Users/86187/Documents/GitHub/Weiczh-s-1st/hw3/figures/' +
                str(choice) + '_train_loss.png')
    # plt.show()
    plt.close()
    # np.savetxt('./ann.csv', records['err_test'], delimiter=',')

    plt.figure(4)
    plt.plot(records['iterations'], records['loss_test'],
             label='loss per hundred iterations')
    min_index = int(np.argmin(records['loss_test']))
    mini = records['loss_test'][min_index]
    plt.plot(min_index * 100, mini, color=color1, marker='o',
             markersize=5, label='loss minimum: ' + str(np.round(mini, 5)))
    plt.title(choice.upper() + '  Test Loss', fontsize=font2)
    plt.legend(loc='upper right')
    plt.xlabel('Number of iterations', fontsize=font3)
    plt.ylabel('Loss value', fontsize=font3)
    plt.tight_layout()
    plt.savefig('C:/Users/86187/Documents/GitHub/Weiczh-s-1st/hw3/figures/' +
                str(choice) + '_test_loss.png')
    # plt.show()
    plt.close()

    # print('time:{}'.format(start))
    # print('iteration:{}'.format(records['iterations'][-1]))
    # print('err_train:{}, err_test:{}'.format(
    #     records['err_train'], records['err_test']))
    # # print('loss_train:{}, loss_test:{}'.format(records['loss_train'], records['loss_test']))
    # print(min_index * 100)


if __name__ == '__main__':
    choice = 'pdn'
    checkpoint = torch.load('check_' + choice + '.pth')
    start = checkpoint['time']
    records = checkpoint['records']

    plotting()
