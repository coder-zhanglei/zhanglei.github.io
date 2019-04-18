#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    QList<QHostAddress> list = QNetworkInterface::allAddresses();
    foreach (QHostAddress address, list)
    {
        if(address.protocol() == QAbstractSocket::IPv4Protocol)
        {
            if(address.toString().contains("127.0.")) continue;

             qDebug() << "Address : " << address.toString();
        }
        else if (address.isNull())  // 主机地址为空
            continue;
    }

}

MainWindow::~MainWindow()
{
    delete ui;
}
