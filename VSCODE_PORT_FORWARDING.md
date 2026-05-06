# 📱 Access ExamGuard on Mobile - VS Code Port Forwarding

## 🚀 Quick Start (3 Minutes)

### **Step 1: Open in VS Code**
```bash
cd c:\mark-1\exam-eye-detection\backend
code .
```

### **Step 2: Start Server**
In VS Code terminal (Ctrl + `):
```bash
python manage.py runserver
```

### **Step 3: Forward Port**
- VS Code shows notification: "Port 8000 is available"
- Click **"Forward Port"**

OR manually:
- Press **Ctrl + Shift + P**
- Type: **"Forward a Port"**
- Enter: **8000**

### **Step 4: Make Public**
In **PORTS** panel (bottom):
- Right-click port **8000**
- Select **"Port Visibility"** → **"Public"**

### **Step 5: Get URL**
Copy the forwarded address:
```
https://abc123-8000.app.github.dev
```

### **Step 6: Open on Phone**
Paste URL in phone browser - Done! ✅

---

## 📋 Detailed Instructions

### **1. Install VS Code (if not installed)**
- Download: https://code.visualstudio.com
- Install and restart

### **2. Open Project**
```bash
# Option A: Command line
cd c:\mark-1\exam-eye-detection\backend
code .

# Option B: VS Code GUI
File → Open Folder → Select backend folder
```

### **3. Open Terminal in VS Code**
- Press **Ctrl + `** (backtick)
- Or: View → Terminal

### **4. Start Django Server**
```bash
python manage.py runserver
```

You'll see:
```
Starting development server at http://127.0.0.1:8000/
```

### **5. Forward the Port**

#### **Automatic Detection:**
VS Code shows notification:
```
Your application running on port 8000 is available
[Open in Browser] [Forward Port]
```
Click **"Forward Port"**

#### **Manual Method:**
1. Press **Ctrl + Shift + P**
2. Type: `Forward a Port`
3. Select: **"Ports: Focus on Ports View"**
4. Click **"+"** button (Forward a Port)
5. Enter: `8000`
6. Press Enter

### **6. Make Port Public**

**IMPORTANT:** By default, ports are private!

1. Look at **PORTS** panel (bottom of VS Code)
2. Find port **8000**
3. Right-click on it
4. Select **"Port Visibility"**
5. Choose **"Public"**

You'll see:
```
Port    Local Address       Visibility    Forwarded Address
8000    localhost:8000      Public        https://abc123-8000.app.github.dev
```

### **7. Copy the URL**
- Click the **globe icon** next to the forwarded address
- Or right-click → **"Copy Forwarded Address"**

### **8. Access from Phone**
1. Open any browser on your phone
2. Paste the URL
3. ✅ ExamGuard loads!

---

## ⚙️ Settings Already Updated

The `settings.py` file has been updated with:

```python
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'https://*.app.github.dev',      # VS Code forwarding
    'https://*.githubpreview.dev',   # VS Code forwarding
]
```

No additional configuration needed!

---

## 🎯 Benefits of VS Code Port Forwarding

✅ **Works Anywhere**
- Not limited to same WiFi
- Access from any device, anywhere
- Share with friends worldwide

✅ **HTTPS Secure**
- Automatic SSL certificate
- No browser warnings
- Green padlock 🔒

✅ **Easy to Use**
- One-click setup
- No firewall configuration
- No router settings

✅ **Free**
- No cost
- No account needed (if using VS Code)
- Unlimited usage

✅ **Fast**
- Low latency
- Direct connection
- No third-party servers

---

## 📱 On Your Phone

Once you access the URL:

### **Features That Work:**
- ✅ Student login
- ✅ Student registration
- ✅ Camera detection (request permission)
- ✅ Face tracking
- ✅ Eye gaze detection
- ✅ All animations
- ✅ Responsive design
- ✅ Touch-friendly interface

### **Add to Home Screen:**
1. Open site in browser
2. Tap menu (⋮ or share icon)
3. Select "Add to Home Screen"
4. Icon appears on home screen
5. Works like a native app!

---

## 🔧 Troubleshooting

### **Port Not Detected?**
- Make sure server is running
- Check terminal for errors
- Try restarting VS Code

### **Can't Make Port Public?**
- You need to be signed in to GitHub in VS Code
- Go to: Accounts (bottom left) → Sign in with GitHub

### **URL Not Working?**
- Check port visibility is "Public"
- Restart the server
- Try a different browser

### **CSRF Error?**
- Settings already updated
- Restart Django server
- Clear browser cache

### **Camera Not Working on Phone?**
- Grant camera permissions in browser
- Use HTTPS URL (not HTTP)
- Try Chrome or Safari

---

## 🆚 Comparison with Other Methods

| Method | Setup | Works Anywhere | HTTPS | Free |
|--------|-------|----------------|-------|------|
| **VS Code** | 2 min | ✅ Yes | ✅ Yes | ✅ Yes |
| Same WiFi | 2 min | ❌ No | ❌ No | ✅ Yes |
| Ngrok | 5 min | ✅ Yes | ✅ Yes | ✅ Yes (limited) |
| PythonAnywhere | 30 min | ✅ Yes | ✅ Yes | ✅ Yes |

---

## 💡 Pro Tips

### **Keep URL Active:**
- Keep VS Code open
- Keep server running
- Don't close terminal

### **Share with Friends:**
- Copy the forwarded URL
- Send via WhatsApp/Email
- They can access from anywhere!

### **Multiple Devices:**
- Same URL works on all devices
- Desktop, laptop, tablet, phone
- No limit on connections

### **Development:**
- Make code changes
- Save file
- Page auto-reloads
- See changes instantly

---

## 🎬 Quick Video Guide

**Step-by-step:**
1. Open VS Code → Open backend folder
2. Terminal → `python manage.py runserver`
3. Click "Forward Port" notification
4. Right-click port 8000 → "Public"
5. Copy URL → Open on phone
6. Done! 🎉

---

## 📞 Need Help?

### **VS Code Not Installed?**
Download: https://code.visualstudio.com

### **Python Not Found?**
Make sure Python is in PATH:
```bash
python --version
```

### **Port Already in Use?**
Kill existing process:
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

---

## 🚀 Alternative: Use Batch File

Double-click: `START_WITH_VSCODE.bat`

It will:
1. Open VS Code
2. Show instructions
3. Guide you through setup

---

## ✅ Checklist

- [ ] VS Code installed
- [ ] Project opened in VS Code
- [ ] Server running (`python manage.py runserver`)
- [ ] Port 8000 forwarded
- [ ] Port visibility set to "Public"
- [ ] URL copied
- [ ] Opened on phone
- [ ] Camera permissions granted
- [ ] ExamGuard working!

---

## 🎉 Success!

Your ExamGuard is now accessible on your phone via VS Code port forwarding!

**URL Format:**
```
https://abc123-8000.app.github.dev
```

**Share this URL with anyone, anywhere!** 🌍

---

## 📊 What's Next?

### **For Permanent Hosting:**
Deploy to PythonAnywhere:
- Follow: `PYTHONANYWHERE_DEPLOYMENT.md`
- Get permanent URL
- No need to keep computer on
- Professional hosting

### **For Quick Testing:**
VS Code port forwarding is perfect!
- Fast setup
- Easy to use
- Works great for demos

---

**ExamGuard - Now accessible on mobile via VS Code!** 📱✅
