// src/components/Header.jsx
import { useState } from 'react';

function Header({ onColetaFinalizada }) {
  const [inputPalavra, setInputPalavra] = useState('');
  const [status, setStatus] = useState('');
  const [placeholderMsg, setPlaceholderMsg] = useState('Buscar vaga...');

  const buscarComStream = () => {
    const palavra = inputPalavra.trim();
    if (!palavra) return alert("Digite uma palavra para buscar.");

    const eventSource = new EventSource(
      `http://localhost:8000/api/stream-coletar-vagas/?palavra=${encodeURIComponent(palavra)}`
    );

    setPlaceholderMsg('⌛ Iniciando busca...');
    setStatus("buscando");

    eventSource.onmessage = (event) => {
      setPlaceholderMsg(event.data);

      if (event.data.toLowerCase().includes("coleta finalizada")) {
        eventSource.close();
        setStatus("finalizado");

        if (onColetaFinalizada) onColetaFinalizada();

        const timeout = setTimeout(() => {
          setPlaceholderMsg("Buscar vaga...");
          setStatus("");
          clearTimeout(timeout);
        }, 4000);
      }
    };

    eventSource.onerror = () => {
      setPlaceholderMsg("❌ Erro na conexão com o servidor");
      eventSource.close();
      setStatus("erro");

      setTimeout(() => {
        setPlaceholderMsg('Buscar vaga...');
      }, 4000);
    };
  };

  return (
    <header className="bg-[#13293D] text-white p-4 flex flex-col gap-2 shadow-md">
      <div className="flex justify-between items-center">
        <div className="flex items-center gap-2">
          <img
            src="/robot-icon.png"
            alt="AutoJobs Logo"
            className="w-12 h-12 -mt-1"
          />
          <h1 className="text-3xl font-bold tracking-wide">AutoJobs</h1>
        </div>

        <div className="flex flex-col items-end gap-1">
          <div className="flex gap-2 items-center">
            <input
              type="text"
              placeholder="Buscar vaga..."
              value={inputPalavra}
              onChange={(e) => setInputPalavra(e.target.value)}
              className="px-4 py-2 rounded-md text-black w-64"
            />
            <button
              onClick={buscarComStream}
              disabled={status === "buscando"}
              className={`px-4 py-2 rounded-md font-medium text-white transition ${
                status === "buscando"
                  ? "bg-gray-500 cursor-not-allowed"
                  : "bg-[#006494] hover:bg-[#247BA0]"
              }`}
            >
              {status === "buscando" ? "Buscando..." : "Buscar"}
            </button>
          </div>

          {(status === "buscando" || status === "finalizado" || status === "erro") && (
            <div className="text-sm mt-1 text-white italic text-right w-full max-w-xs truncate">
              {placeholderMsg}
            </div>
          )}
        </div>
      </div>
    </header>
  );
}

export default Header;
