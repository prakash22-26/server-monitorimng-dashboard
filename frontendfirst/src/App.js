import React, { useEffect, useState } from "react";
import {
  BarChart,
  Bar,
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

export default function ServerMonitoringDashboard() {
  const [alertCounts, setAlertCounts] = useState({});
  const [dynamicUsage, setDynamicUsage] = useState([]);
  const [dynamicTraffic, setDynamicTraffic] = useState([]);
  const [servers, setServers] = useState([]);

  useEffect(() => {
    const socket = new WebSocket(
      "https://server-monitorimng-dashboard-1.onrender.com"
    );

    socket.onopen = () => {
      console.log("WebSocket connection established");
    };

    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setAlertCounts(data.alerts);
      setDynamicUsage(data.usage);
      setServers(data.servers);
      setDynamicTraffic((prevTraffic) => {
        const updated = [...prevTraffic, data.networkTraffic];
        return updated.length > 20 ? updated.slice(-20) : updated;
      });
    };

    socket.onerror = (err) => {
      console.error("WebSocket error:", err);
    };

    socket.onclose = () => {
      console.log("WebSocket connection closed");
    };

    return () => {
      socket.close();
    };
  }, []);

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-8">
      <h1 className="text-4xl font-bold text-gray-800 mb-6">
        Server Monitoring Dashboard
      </h1>

      {/* Alerts */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-6">
        {Object.entries(alertCounts).map(([level, count]) => (
          <div
            key={level}
            className="bg-white p-6 rounded-2xl shadow-lg hover:shadow-xl transition-all"
          >
            <h2 className="text-xl font-semibold capitalize text-gray-600">
              {level} Alerts
            </h2>
            <p className="text-4xl font-bold text-center text-indigo-600 mt-2">
              {count}
            </p>
          </div>
        ))}
      </div>

      {/* Resource Usage */}
      <div className="bg-white rounded-2xl shadow-lg p-6 mb-6">
        <h2 className="text-xl font-semibold text-gray-700 mb-4">
          Resource Usage
        </h2>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={dynamicUsage}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="value" fill="#6366f1" radius={[4, 4, 0, 0]} />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* Network Traffic */}
      <div className="bg-white rounded-2xl shadow-lg p-6 mb-6">
        <h2 className="text-xl font-semibold text-gray-700 mb-4">
          Incoming Network Traffic
        </h2>
        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={dynamicTraffic}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="time" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Line
              type="monotone"
              dataKey="traffic"
              stroke="#10b981"
              strokeWidth={3}
              dot={false}
            />
          </LineChart>
        </ResponsiveContainer>
      </div>

      {/* Server Table */}
      <div className="bg-white rounded-2xl shadow-lg p-6">
        <h2 className="text-xl font-semibold text-gray-700 mb-4">Servers</h2>
        <div className="overflow-x-auto">
          <table className="min-w-full border-collapse">
            <thead>
              <tr className="bg-indigo-100 text-gray-700">
                <th className="p-3 text-left font-semibold">ID</th>
                <th className="p-3 text-left font-semibold">Name</th>
                <th className="p-3 text-left font-semibold">IP Address</th>
                <th className="p-3 text-left font-semibold">Status</th>
              </tr>
            </thead>
            <tbody>
              {servers.map((server, i) => (
                <tr
                  key={server.id}
                  className={`hover:bg-indigo-50 ${
                    i % 2 === 0 ? "bg-gray-50" : "bg-white"
                  }`}
                >
                  <td className="p-3">{server.id}</td>
                  <td className="p-3">{server.name}</td>
                  <td className="p-3">{server.ip}</td>
                  <td className="p-3">
                    <span
                      className={`font-semibold ${
                        server.status === "Online"
                          ? "text-green-600"
                          : "text-red-600"
                      }`}
                    >
                      {server.status}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
