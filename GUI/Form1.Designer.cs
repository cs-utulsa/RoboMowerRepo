namespace LawnGui
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing) {
            if (disposing && (components != null)) {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent() {
            this.btnUpload = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.txbFilePath = new System.Windows.Forms.TextBox();
            this.picbUpload = new System.Windows.Forms.PictureBox();
            this.label2 = new System.Windows.Forms.Label();
            this.btn_temp1 = new System.Windows.Forms.Button();
            this.btn_temp2 = new System.Windows.Forms.Button();
            this.btn_temp3 = new System.Windows.Forms.Button();
            this.btn_temp4 = new System.Windows.Forms.Button();
            this.btn_runMower = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.picbUpload)).BeginInit();
            this.SuspendLayout();
            // 
            // btnUpload
            // 
            this.btnUpload.Location = new System.Drawing.Point(16, 11);
            this.btnUpload.Name = "btnUpload";
            this.btnUpload.Size = new System.Drawing.Size(170, 34);
            this.btnUpload.TabIndex = 0;
            this.btnUpload.Text = "Upload Image";
            this.btnUpload.UseVisualStyleBackColor = true;
            this.btnUpload.Click += new System.EventHandler(this.btnUpload_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(219, 14);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(38, 25);
            this.label1.TabIndex = 1;
            this.label1.Text = "File";
            // 
            // txbFilePath
            // 
            this.txbFilePath.Location = new System.Drawing.Point(263, 14);
            this.txbFilePath.Name = "txbFilePath";
            this.txbFilePath.Size = new System.Drawing.Size(662, 31);
            this.txbFilePath.TabIndex = 2;
            // 
            // picbUpload
            // 
            this.picbUpload.Location = new System.Drawing.Point(23, 110);
            this.picbUpload.Name = "picbUpload";
            this.picbUpload.Size = new System.Drawing.Size(489, 438);
            this.picbUpload.TabIndex = 3;
            this.picbUpload.TabStop = false;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.BackColor = System.Drawing.SystemColors.Control;
            this.label2.Enabled = false;
            this.label2.Location = new System.Drawing.Point(672, 82);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(144, 25);
            this.label2.TabIndex = 6;
            this.label2.Text = "Saved Templates";
            this.label2.Click += new System.EventHandler(this.label2_Click);
            // 
            // btn_temp1
            // 
            this.btn_temp1.Location = new System.Drawing.Point(555, 110);
            this.btn_temp1.Name = "btn_temp1";
            this.btn_temp1.Size = new System.Drawing.Size(173, 183);
            this.btn_temp1.TabIndex = 9;
            this.btn_temp1.UseVisualStyleBackColor = true;
            this.btn_temp1.Click += new System.EventHandler(this.btn_temp1_Click);
            // 
            // btn_temp2
            // 
            this.btn_temp2.Location = new System.Drawing.Point(752, 110);
            this.btn_temp2.Name = "btn_temp2";
            this.btn_temp2.Size = new System.Drawing.Size(173, 183);
            this.btn_temp2.TabIndex = 10;
            this.btn_temp2.UseVisualStyleBackColor = true;
            this.btn_temp2.Click += new System.EventHandler(this.btn_temp2_Click);
            // 
            // btn_temp3
            // 
            this.btn_temp3.Location = new System.Drawing.Point(555, 318);
            this.btn_temp3.Name = "btn_temp3";
            this.btn_temp3.Size = new System.Drawing.Size(173, 183);
            this.btn_temp3.TabIndex = 11;
            this.btn_temp3.UseVisualStyleBackColor = true;
            this.btn_temp3.Click += new System.EventHandler(this.btn_temp3_Click);
            // 
            // btn_temp4
            // 
            this.btn_temp4.Location = new System.Drawing.Point(752, 318);
            this.btn_temp4.Name = "btn_temp4";
            this.btn_temp4.Size = new System.Drawing.Size(173, 183);
            this.btn_temp4.TabIndex = 12;
            this.btn_temp4.UseVisualStyleBackColor = true;
            this.btn_temp4.Click += new System.EventHandler(this.btn_temp4_Click);
            // 
            // btn_runMower
            // 
            this.btn_runMower.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.btn_runMower.Location = new System.Drawing.Point(16, 633);
            this.btn_runMower.Name = "btn_runMower";
            this.btn_runMower.Size = new System.Drawing.Size(170, 34);
            this.btn_runMower.TabIndex = 13;
            this.btn_runMower.Text = "Run Mower";
            this.btn_runMower.UseVisualStyleBackColor = true;
            this.btn_runMower.Click += new System.EventHandler(this.btn_runMower_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(10F, 25F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(964, 679);
            this.Controls.Add(this.btn_runMower);
            this.Controls.Add(this.btn_temp4);
            this.Controls.Add(this.btn_temp3);
            this.Controls.Add(this.btn_temp2);
            this.Controls.Add(this.btn_temp1);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.picbUpload);
            this.Controls.Add(this.txbFilePath);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.btnUpload);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.picbUpload)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private Button btnUpload;
        private Label label1;
        private TextBox txbFilePath;
        private PictureBox picbUpload;
        private Label label2;
        private Button btn_temp1;
        private Button btn_temp2;
        private Button btn_temp3;
        private Button btn_temp4;
        private Button btn_runMower;
    }
}