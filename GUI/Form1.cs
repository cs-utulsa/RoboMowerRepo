using Renci.SshNet;
using System.Drawing;
using System.Reflection;
using System.Windows.Forms;
using System.Configuration;
using System.Collections.Specialized;
using static System.Windows.Forms.AxHost;

namespace LawnGui
{
    public partial class Form1 : Form
    {
        public Form1() {
            InitializeComponent();


            Image im = Image.FromFile("../../../templates/test1.png");
            btn_temp1.Image = (Image)(new Bitmap(im, new Size(btn_temp1.Width, btn_temp1.Height)));
            im = Image.FromFile("../../../templates/test2.png");
            btn_temp2.Image = (Image)(new Bitmap(im, new Size(btn_temp2.Width, btn_temp2.Height)));
            im = Image.FromFile("../../../templates/test3.png");
            btn_temp3.Image = (Image)(new Bitmap(im, new Size(btn_temp3.Width, btn_temp3.Height)));
            im = Image.FromFile("../../../templates/test4.png");
            btn_temp4.Image = (Image)(new Bitmap(im, new Size(btn_temp4.Width, btn_temp4.Height)));
        }

        private void btnUpload_Click(object sender, EventArgs e) {
            //txbFilePath.Text = "hi";
            OpenFileDialog openFile = new OpenFileDialog {
                Title = "Browse Images",
                CheckFileExists = true,
                CheckPathExists = true,
                Filter = "Images (*.BMP;*.JPG;*.GIF;*.PNG;*.TIFF)|*.BMP;*.JPG;*.GIF;*.PNG;*.TIFF|" +
                "All files (*.*)|*.*",
                FilterIndex = 2,
                RestoreDirectory = true,
                ReadOnlyChecked = true,
                ShowReadOnly = true,
            };

            if (openFile.ShowDialog() == DialogResult.OK) {
                txbFilePath.Text = openFile.FileName;
                Bitmap myBitmap = new Bitmap(openFile.FileName);

                SetPreviewBox(myBitmap);
            }

        }

        private void listView1_SelectedIndexChanged(object sender, EventArgs e) {

        }

        private void label2_Click(object sender, EventArgs e) {

        }

        private void SetPreviewBox(Bitmap bp) {
            picbUpload.Image = MakeGrayscale(bp);
            picbUpload.BorderStyle = BorderStyle.FixedSingle;
            picbUpload.SizeMode = PictureBoxSizeMode.StretchImage;
        }

        private void btn_temp1_Click(object sender, EventArgs e) {
            Bitmap myBitmap = new Bitmap(btn_temp1.Image);
            SetPreviewBox(myBitmap);
            /*Image im = Image.FromFile("../../../templates/test1.png");
            btn_temp1.Image = (Image)(new Bitmap(im,new Size(btn_temp1.Width,btn_temp1.Height)) );*/
        }

        private void btn_temp2_Click(object sender, EventArgs e) {
            Bitmap myBitmap = new Bitmap(btn_temp2.Image);
            SetPreviewBox(myBitmap);
        }

        private void btn_temp3_Click(object sender, EventArgs e) {
            Bitmap myBitmap = new Bitmap(btn_temp3.Image);
            SetPreviewBox(myBitmap);
        }

        private void btn_temp4_Click(object sender, EventArgs e) {
            Bitmap myBitmap = new Bitmap(btn_temp4.Image);
            SetPreviewBox(myBitmap);
        }

        private void btn_runMower_Click(object sender, EventArgs e) {
            if (picbUpload.Image == null) return;

            // make grayscale, save to data
            Bitmap bitm = new Bitmap(picbUpload.Image);
            bitm = MakeGrayscale(bitm);
            Image im = (Image)(bitm);
            im.Save("../../../data/processImage.png");

            // do the stuff to send it to the next layer
            string ip_address = ConfigurationManager.AppSettings.Get("HubIP");
            string localFilePath = "../../../data/processImage.png";
            string remoteFilePath = ConfigurationManager.AppSettings.Get("RemoteFilePath");
            string username = ConfigurationManager.AppSettings.Get("Username");
            string password = ConfigurationManager.AppSettings.Get("Password");

            //Uploading File
            using (ScpClient client = new ScpClient(ip_address, username, password)) {
                try {
                    client.Connect();

                    using (Stream localFile = File.OpenRead(localFilePath)) {
                        client.Upload(localFile, remoteFilePath);
                    }
                }
                catch (Exception ex) {
                    MessageBox.Show(ex.Message);
                }
            }
        }

        private Bitmap MakeGrayscale(Bitmap bp) {
            // setup
            int width = bp.Width;
            int height = bp.Height;
            Color p;

            // go thru x values
            for (int x = 0; x < width; x++) {
                // go thru y values
                for (int y = 0; y < height; y++) {
                    // get pixel value
                    p = bp.GetPixel(x, y);

                    // extract color component values
                    int a = p.A;
                    int r = p.R;
                    int g = p.G;
                    int b = p.B;

                    //find average
                    int avg = (r + g + b) / 3;
                    if (avg > 255 / 2) avg = 255;
                    else avg = 0;

                    // set new pixel value
                    bp.SetPixel(x, y, Color.FromArgb(a, avg, avg, avg));
                }
            }

            // return modified bitmap
            return bp;
        }
    }
}