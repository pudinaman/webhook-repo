import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Github, PlayCircle, GitPullRequest, GitMerge, Clock } from 'lucide-react';

const API_BASE_URL = 'http://127.0.0.1:5000/api/actions';

const App = () => {
  const [actions, setActions] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchActions = async () => {
    try {
      const response = await axios.get(API_BASE_URL);
      setActions(response.data);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching actions:', error);
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchActions();
    const interval = setInterval(fetchActions, 15000);
    return () => clearInterval(interval);
  }, []);

  const getIcon = (type) => {
    switch (type) {
      case 'PUSH': return <PlayCircle className="text-indigo-400" size={20} />;
      case 'PULL_REQUEST': return <GitPullRequest className="text-amber-400" size={20} />;
      case 'MERGE': return <GitMerge className="text-emerald-400" size={20} />;
      default: return <Github className="text-gray-400" size={20} />;
    }
  };

  return (
    <div className="min-h-screen py-10 px-4 sm:px-6 lg:px-8 flex items-center justify-center">
      <div className="container max-w-3xl w-full glass rounded-[32px] shadow-2xl overflow-hidden flex flex-col max-h-[90vh]">
        <div className="p-8 border-b border-white/10 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="bg-white/10 p-2 rounded-xl">
              <Github className="text-white" size={24} />
            </div>
            <h1 className="text-2xl font-bold text-white tracking-tight">Activity Feed</h1>
          </div>
          <div className="flex items-center gap-2 px-3 py-1 bg-white/5 rounded-full border border-white/10">
            <div className="w-2 h-2 bg-emerald-500 rounded-full animate-pulse"></div>
            <span className="text-xs font-medium text-emerald-500/80 uppercase tracking-wider">Live Polling</span>
          </div>
        </div>

        <div className="flex-1 overflow-y-auto p-6 flex flex-col gap-4 custom-scrollbar">
          {loading && actions.length === 0 ? (
            <div className="flex flex-col items-center justify-center py-20 opacity-40">
              <div className="animate-spin rounded-full h-8 w-8 border-2 border-white/20 border-t-white"></div>
              <p className="mt-4 text-sm">Detecting activity...</p>
            </div>
          ) : actions.length === 0 ? (
            <div className="text-center py-20 opacity-40 italic">
              <p>No activity yet. Trigger a webhook to see it here!</p>
            </div>
          ) : (
            actions.map((action, idx) => (
              <div 
                key={action._id} 
                className="action-item glass rounded-2xl p-5 hover:bg-white/10 transition-all duration-300 group relative border border-white/5"
                style={{ animationDelay: `${idx * 0.05}s` }}
              >
                <div className="flex gap-4 items-start">
                  <div className="mt-1 bg-white/5 p-2 rounded-lg group-hover:bg-white/10 transition-colors">
                    {getIcon(action.request_type)}
                  </div>
                  <div className="flex-1 min-w-0">
                    <p className="text-[1.05rem] leading-relaxed text-gray-200 group-hover:text-white transition-colors">
                      {action.message}
                    </p>
                    <div className="flex items-center gap-2 mt-3 text-sm text-gray-500 font-medium">
                      <Clock size={14} />
                      <span>{action.timestamp}</span>
                    </div>
                  </div>
                </div>
              </div>
            ))
          )}
        </div>
        
        <div className="px-8 py-4 bg-white/5 border-t border-white/10 text-center">
          <p className="text-[10px] uppercase tracking-[0.2em] text-gray-500 font-bold">
            Real-time GitHub Webhook Aggregator
          </p>
        </div>
      </div>
    </div>
  );
};

export default App;
