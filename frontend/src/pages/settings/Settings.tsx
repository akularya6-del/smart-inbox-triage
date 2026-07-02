import { useState, useEffect } from 'react';
import { Settings as SettingsIcon, Save, Bell, Palette, Database } from 'lucide-react';
import { toast } from 'sonner';

export default function Settings() {
  const [isSaving, setIsSaving] = useState(false);
  const [config, setConfig] = useState({
    theme: 'system',
    notifications: false,
    syncInterval: '5',
    maxEmails: '50',
  });

  const handleSave = async () => {
    setIsSaving(true);
    try {
      // In a real app, call API to save settings
      await new Promise(r => setTimeout(r, 600));
      toast.success('Settings saved successfully');
    } catch (e) {
      toast.error('Failed to save settings');
    } finally {
      setIsSaving(false);
    }
  };

  const handleNotificationRequest = async () => {
    if (!("Notification" in window)) {
      toast.error("This browser does not support desktop notification");
      return;
    }
    
    if (Notification.permission === "granted") {
      setConfig({...config, notifications: true});
      toast.success("Notifications enabled");
    } else if (Notification.permission !== "denied") {
      const permission = await Notification.requestPermission();
      if (permission === "granted") {
        setConfig({...config, notifications: true});
        toast.success("Notifications enabled");
      }
    }
  };

  return (
    <div className="flex flex-col h-full space-y-6 max-w-3xl mx-auto">
      <div className="flex justify-between items-center pb-4 border-b border-border">
        <h2 className="text-2xl font-bold tracking-tight flex items-center gap-2">
          <SettingsIcon className="w-6 h-6" /> Settings
        </h2>
        <button 
          onClick={handleSave}
          disabled={isSaving}
          className="flex items-center gap-2 bg-primary text-primary-foreground px-4 py-2 rounded-md font-medium text-sm hover:bg-primary/90 transition-colors disabled:opacity-50"
        >
          <Save className="w-4 h-4" />
          {isSaving ? 'Saving...' : 'Save Changes'}
        </button>
      </div>

      <div className="space-y-8">
        {/* Appearance */}
        <section className="space-y-4">
          <h3 className="text-lg font-semibold flex items-center gap-2">
            <Palette className="w-5 h-5 text-muted-foreground" /> Appearance
          </h3>
          <div className="bg-card border border-border rounded-lg p-4 space-y-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="font-medium">Theme</p>
                <p className="text-sm text-muted-foreground">Select your preferred color theme</p>
              </div>
              <select 
                value={config.theme} 
                onChange={(e) => setConfig({...config, theme: e.target.value})}
                className="bg-secondary border-none rounded-md text-sm px-3 py-2 outline-none"
              >
                <option value="system">System Default</option>
                <option value="light">Light</option>
                <option value="dark">Dark</option>
              </select>
            </div>
          </div>
        </section>

        {/* Sync Settings */}
        <section className="space-y-4">
          <h3 className="text-lg font-semibold flex items-center gap-2">
            <Database className="w-5 h-5 text-muted-foreground" /> Synchronization
          </h3>
          <div className="bg-card border border-border rounded-lg p-4 space-y-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="font-medium">Sync Interval (minutes)</p>
                <p className="text-sm text-muted-foreground">How often to fetch new emails</p>
              </div>
              <input 
                type="number" 
                value={config.syncInterval}
                onChange={(e) => setConfig({...config, syncInterval: e.target.value})}
                className="bg-secondary border-none rounded-md text-sm px-3 py-2 outline-none w-24 text-right"
              />
            </div>
            <div className="flex items-center justify-between">
              <div>
                <p className="font-medium">Max Emails per Sync</p>
                <p className="text-sm text-muted-foreground">Limit the batch size per sync cycle</p>
              </div>
              <input 
                type="number" 
                value={config.maxEmails}
                onChange={(e) => setConfig({...config, maxEmails: e.target.value})}
                className="bg-secondary border-none rounded-md text-sm px-3 py-2 outline-none w-24 text-right"
              />
            </div>
          </div>
        </section>

        {/* Notifications */}
        <section className="space-y-4">
          <h3 className="text-lg font-semibold flex items-center gap-2">
            <Bell className="w-5 h-5 text-muted-foreground" /> Notifications
          </h3>
          <div className="bg-card border border-border rounded-lg p-4 space-y-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="font-medium">Browser Notifications</p>
                <p className="text-sm text-muted-foreground">Get alerted for urgent emails and review items</p>
              </div>
              <button 
                onClick={handleNotificationRequest}
                className={`px-3 py-1.5 rounded-md text-sm font-medium transition-colors ${config.notifications ? 'bg-success/20 text-success' : 'bg-secondary text-secondary-foreground hover:bg-secondary/80'}`}
              >
                {config.notifications ? 'Enabled' : 'Enable'}
              </button>
            </div>
          </div>
        </section>
      </div>
    </div>
  );
}
