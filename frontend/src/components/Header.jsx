// src/components/Header.jsx
function Header() {
  return (
    <header className="bg-[#13293D] text-white p-4 flex justify-between items-center shadow-md">
      <h1 className="text-xl font-bold">AutoJobs</h1>
      <div className="flex gap-2">
        <input
          type="text"
          placeholder="Buscar vaga..."
          className="px-3 py-2 rounded-md text-black w-64"
        />
        <button className="bg-[#006494] text-white font-medium px-4 py-2 rounded-md hover:bg-[#247BA0]">
          Buscar
        </button>
      </div>
    </header>
  );
}

export default Header;
