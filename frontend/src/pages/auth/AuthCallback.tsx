import { useEffect, useState } from 'react';
import { useNavigate, useSearchParams } from 'react-router-dom';
import { auth } from '../../lib/api';
import { Loader2 } from 'lucide-react';
import { toast } from 'sonner';

export default function AuthCallback() {
  const [searchParams] = useSearchParams();
  const navigate = useNavigate();
  const [status, setStatus] = useState("Exchanging secure token...");

  useEffect(() => {
    const code = searchParams.get('code');
    if (!code) {
      toast.error('No authorization code found.');
      navigate('/login');
      return;
    }

    const exchangeToken = async () => {
      try {
        await auth.callback(code);
        toast.success('Successfully connected to Google!');
        navigate('/');
      } catch (err) {
        console.error(err);
        toast.error('Failed to authenticate with server.');
        navigate('/login');
      }
    };

    exchangeToken();
  }, [searchParams, navigate]);

  return (
    <div className="min-h-screen flex items-center justify-center bg-background">
      <div className="flex flex-col items-center gap-4 text-muted-foreground">
        <Loader2 className="w-8 h-8 animate-spin text-primary" />
        <p className="text-sm font-medium animate-pulse">{status}</p>
      </div>
    </div>
  );
}
